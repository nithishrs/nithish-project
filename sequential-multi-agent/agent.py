"""Startup Pitch Deck Generator - A sequential multi-agent system that researches markets, analyzes competition, and creates pitch decks.

This demonstrates how to chain multiple agents together in sequence, where each agent
processes the output of the previous agent to build a comprehensive deliverable.
"""

from google.adk.agents import Agent, SequentialAgent
from google.adk.tools import google_search

from . import prompt

# Step 1: Market Researcher - Gathers market data and industry information
market_researcher = Agent(
    name="market_researcher",
    model="gemini-2.5-flash",
    description="Researches market size, trends, and industry information for a startup idea",
    instruction=prompt.MARKET_RESEARCHER_INSTRUCTION,
    tools=[google_search],
    output_key="market_research",
)

# Step 2: Competitive Analyst - Analyzes competitors and market positioning
competitive_analyst = Agent(
    name="competitive_analyst",
    model="gemini-2.5-flash",
    description="Analyzes competitors, identifies market gaps, and determines competitive positioning",
    instruction=prompt.COMPETITIVE_ANALYST_INSTRUCTION,
    output_key="competitive_analysis",
)

# Step 3: Pitch Deck Creator - Creates a professional pitch deck
pitch_deck_creator = Agent(
    name="pitch_deck_creator",
    model="gemini-2.5-flash",
    description="Creates a comprehensive startup pitch deck from market research and competitive analysis",
    instruction=prompt.PITCH_DECK_CREATOR_INSTRUCTION,
)

# Sequential Pipeline: Research Market -> Analyze Competition -> Create Pitch Deck
pitch_deck_pipeline = SequentialAgent(
    name="pitch_deck_pipeline",
    description="A sequential pipeline that researches markets, analyzes competition, and creates a startup pitch deck",
    sub_agents=[
        market_researcher,      # Step 1: Research market
        competitive_analyst,    # Step 2: Analyze competition
        pitch_deck_creator,    # Step 3: Create pitch deck
    ],
)

# Root Agent: Orchestrates the pitch deck generation
root_agent = Agent(
    name="startup_pitch_deck_generator",
    model="gemini-2.5-flash",
    description="A multi-agent system that helps entrepreneurs create professional pitch decks by researching markets, analyzing competition, and generating comprehensive pitch materials",
    instruction="""You are a startup pitch deck assistant. Your role is to help entrepreneurs create compelling pitch decks for their startup ideas.

**Your Process:**
1. Greet the user warmly and ask about their startup idea
2. Collect key information:
   - What problem does their startup solve?
   - What is their solution/product?
   - Who is their target market?
   - What makes them unique?
3. Store the startup idea details in session state under the key `startup_idea`
4. Delegate to the pitch_deck_pipeline to:
   - Research the market opportunity
   - Analyze competitors and positioning
   - Create a comprehensive pitch deck
5. Present the final pitch deck to the user

**Your Personality:**
- Be enthusiastic and supportive - starting a company is exciting!
- Ask clarifying questions to understand their vision
- Show genuine interest in their idea
- Be encouraging throughout the process

When the user provides their startup idea, acknowledge it enthusiastically and start the pitch deck generation process by delegating to the pitch_deck_pipeline agent.""",
    sub_agents=[pitch_deck_pipeline],
)

