import re
import io
from contextlib import redirect_stdout
import streamlit as st
from agent_team_updated import agent_team

# Regex that matches ANSI escape sequences
ANSI_ESCAPE = re.compile(r'(?:\x1B\[.*?m)')

def run_agent_clean_output(prompt: str) -> str:
    buf = io.StringIO()
    # Capture stdout from the agent’s print_response
    with redirect_stdout(buf):
        agent_team.print_response(prompt, stream=True)
    raw_output = buf.getvalue()
    # Strip out ANSI color codes
    cleaned_output = ANSI_ESCAPE.sub('', raw_output)
    return cleaned_output

def main():
    st.title("Finance Investment Agent")

    # Let user pick a stock
    stocks = ["NVDA", "AAPL", "TSLA", "GOOG"]
    chosen_stock = st.selectbox("Select a stock symbol", stocks)

    # Let user pick a display approach for the output
    display_options = ["Markdown", "Text", "Code Block"]
    display_choice = st.selectbox("How do you want to display the output?", display_options)

    if st.button("Get Info"):
        prompt = f"Summarize analyst recommendations and share the latest news for {chosen_stock}"
        result = run_agent_clean_output(prompt)

        if display_choice == "Markdown":
            # Interprets headings, bullet points, tables, etc.
            st.markdown(result)
        elif display_choice == "Text":
            # Shows raw text with monospaced font (like a console)
            st.text(result)
        elif display_choice == "Code Block":
            # Monospaced code block with no syntax highlighting
            st.code(result, language="")

if __name__ == "__main__":
    main()
