from agno.agent import Agent
from agno.models.deepseek import DeepSeek
from agno.models.anthropic import Claude
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["ANTHROPIC_API_KEY"]=os.getenv("ANTHROPIC_API_KEY")
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

web_agent=Agent(
    name="Web Agent",
    role="search the web for information",
    model=Claude(id="claude-3-7-sonnet-20250219"),
    tools=[DuckDuckGoTools()],
    instructions="Always include the sources",
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=Claude(id="claude-3-7-sonnet-20250219"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True,stock_fundamentals=True,company_info=True)],
    instructions="Use tables to display data",
    show_tool_calls=True,
    markdown=True,
)

agent_team=Agent(
    team=[web_agent,finance_agent],
    model=Claude(id="claude-3-7-sonnet-20250219"),
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,

)

agent_team.print_response("Analyze companies like Tesla,NVDA,Apple and suggest which to buy for long term")