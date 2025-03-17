from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.anthropic import Claude
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.models.deepseek import DeepSeek

import os
from dotenv import load_dotenv
load_dotenv()
os.environ["ANTHROPIC_API_KEY"]=os.getenv("ANTHROPIC_API_KEY")
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")


agent=Agent(
    model=Claude(id="claude-3-7-sonnet-20250219"),
    description="You are an assistant please reply based ont he question",
    tools=[DuckDuckGoTools()],
    markdown=True
)

agent.print_response("Who won the India vs Newzealand finals in CT 2025")