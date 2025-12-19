"""Tech News Researcher - An agent that finds the latest tech news and product information."""

from google.adk.agents import Agent
from google.adk.tools import google_search

from . import prompt

root_agent = Agent(
    name="tech_news_researcher",
    model="gemini-2.5-flash",
    description="A tech news researcher that finds the latest information about technology, products, startups, and industry trends.",
    instruction=prompt.SEARCH_AGENT_PROMPT,
    tools=[google_search],
)

