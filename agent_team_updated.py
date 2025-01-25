from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

# Web Agent
web_agent = Agent(
    # Newer signature uses provider=... instead of model=...
    provider=Groq(id="llama-3.3-70b-versatile"),
    agent_id="web-agent",
    name="Web Agent",
    session_id="session_web",

    # Key parameters that help reproduce your older script's behavior:
    add_chat_history_to_messages=True,
    knowledge_base=None,
    add_references=False,             # or True if you want references
    references_format="json",         # only applies if add_references=True
    output_model=None,
    debug_mode=False,                  # often helps show “Running:” or step logs
    show_tool_calls=True,            # prints the calls to sub-tools or sub-agents
    markdown=True,                   # keeps Markdown formatting in output

    # The instructions you originally used
    instructions=["Always include sources"],

    # The same tools as before
    tools=[DuckDuckGo()],
)

# Finance Agent
finance_agent = Agent(
    provider=Groq(id="llama-3.3-70b-versatile"),
    agent_id="finance-agent",
    name="Finance Agent",
    session_id="session_finance",

    add_chat_history_to_messages=True,
    knowledge_base=None,
    add_references=False,
    references_format="json",
    output_model=None,
    debug_mode=False,
    show_tool_calls=True,
    markdown=True,

    # Combine your old "role" message with instructions (the new signature
    # may not have a dedicated 'role' param)
    instructions=[
        "Get financial data",
        "Use tables to display data"
    ],

    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            company_info=True,
            historical_prices=True
        )
    ],
)

# “Team” Agent orchestrating sub-agents
agent_team = Agent(
    provider=Groq(id="llama-3.3-70b-versatile"),
    agent_id="agent-team",
    name="Agent Team",
    session_id="session_team",

    add_chat_history_to_messages=True,
    knowledge_base=None,
    add_references=False,
    references_format="json",
    output_model=None,
    debug_mode=False,         # enables more verbose “Running:” or steps
    show_tool_calls=True,
    markdown=True,
    
    # Combined instructions
    instructions=[
        "Always include sources",
        "Use tables to display data"
    ],
    
    # The sub-agents that do web+finance tasks
    team=[web_agent, finance_agent],
)

if __name__ == "__main__":
    # Test the final agent
    agent_team.print_response(
        "Summarize analyst recommendations and share the latest news for NVDA",
        stream=True
    )
