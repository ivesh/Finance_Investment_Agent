from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

# Example web agent
web_agent = Agent(
    provider=Groq(id="llama-3.3-70b-versatile"),
    agent_id="web-agent",
    name="Web Agent",
    session_id="session_web",
    # Pylance-required flags
    add_chat_history_to_messages=True,
    knowledge_base=None,
    add_references=False,
    references_format="json",
    output_model=None,
    debug_mode=False,
    # other fields that still exist
    instructions=["Always include sources"],
    tools=[DuckDuckGo()],
    # etc.
)

# Example finance agent
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
    instructions=["Use tables to display data"],
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            company_info=True
        )
    ],
)

# Example “team” agent
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
    debug_mode=False,
    instructions=[
        "Always include sources",
        "Use tables to display data"
    ],
    # If your version still supports sub-agents via a `team` or `agents` param:
    team=[web_agent, finance_agent],
)

# Now call your prompt
if __name__ == "__main__":
    agent_team.print_response(
        "Summarize analyst recommendations and share the latest news for NVDA",
        stream=True
    )
