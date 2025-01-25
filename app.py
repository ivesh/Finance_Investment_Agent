import streamlit as st
import io
import re
from contextlib import redirect_stdout
from agent_team_updated import agent_team

# Regex to strip out ANSI color codes
ANSI_ESCAPE = re.compile(r'(?:\x1B\[.*?m)')

def run_agent_clean_output(prompt: str) -> str:
    """
    Calls agent_team.print_response(prompt, stream=True),
    captures all printed text, and strips ANSI color codes.
    """
    buf = io.StringIO()
    with redirect_stdout(buf):
        agent_team.print_response(prompt, stream=True)
    raw_output = buf.getvalue()
    return ANSI_ESCAPE.sub('', raw_output)

def main():
    st.title("Finance Investment Agent")

    # Keep list of messages (chat) in session state
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    # ----------------- SIDEBAR ----------------------
    st.sidebar.title("Conversation History")

    # Wrap the conversation display in an expander, so we can scroll if it's large
    with st.sidebar.expander("Show/Hide Full Chat", expanded=True):
        if st.session_state["messages"]:
            for msg in st.session_state["messages"]:
                if msg["role"] == "user":
                    st.markdown(f"**User:** {msg['content']}")
                else:  # assistant
                    # If the message is very large, you could truncate it
                    st.markdown(f"**Agent:**\n```\n{msg['content'][:600]}...\n```")
        else:
            st.write("No conversation yet.")

    # ----------------- MAIN PAGE ----------------------
    # Provide a text input for the user’s prompt
    # Let user pick a stock
    stocks = ["NVDA", "AAPL", "TSLA", "GOOG"]
    chosen_stock = st.selectbox("Select a stock symbol", stocks)

    user_input = st.text_input("Enter a prompt for the Agent (e.g. 'Summarize analyst recommendations for NVDA')")

    if st.button("Send Prompt"):
        if not user_input.strip():
            st.warning("Please enter a valid prompt.")
        else:
            # Add user message to chat history
            st.session_state["messages"].append({"role": "user", "content": user_input, "stock": chosen_stock})

            # Get the agent's console-style output
            response_text = run_agent_clean_output(user_input)

            # Add the response to chat history
            st.session_state["messages"].append({"role": "assistant", "content": response_text})

    # If there's at least one response in the conversation, show the last one on the main page
    # (so you see the newest result up front).
    if st.session_state["messages"]:
        last_message = st.session_state["messages"][-1]
        if last_message["role"] == "assistant":
            st.subheader("Latest Agent Response")
            # Show the entire final text in a code block
            st.code(last_message["content"], language="")

if __name__ == "__main__":
    main()
