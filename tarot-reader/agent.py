"""Tarot Reader - A multi-agent system that draws tarot cards and provides validated, beautifully formatted interpretations.

This demonstrates a sequential multi-agent pattern with iterative refinement:
1. Cards are drawn using a custom tool
2. An interpreter creates a reading based on the cards and user's question
3. A strict validator reviews the interpretation using web search to verify card meanings
4. The interpreter and validator loop until the validator fully approves (max 4 iterations)
5. A formatter creates a visually stunning presentation with ASCII art
"""

from google.adk.agents import Agent, SequentialAgent, LoopAgent
from google.adk.tools import FunctionTool, google_search

from .tarot_tool import draw_tarot_cards
from . import prompt

# Step 1: Interpreter Agent - Creates interpretation of the cards
interpreter_agent = Agent(
    name="tarot_interpreter",
    model="gemini-2.5-flash",
    description="Interprets tarot cards in relation to the user's question, creating a meaningful reading. Revises interpretation based on validator feedback.",
    instruction=prompt.INTERPRETER_INSTRUCTION,
    output_key="tarot_interpretation",
)

# Step 2: Validator Agent - Strictly reviews interpretation for accuracy using web search
validator_agent = Agent(
    name="tarot_validator",
    model="gemini-2.5-pro",  # Use pro model for more rigorous validation
    description="Strictly validates that the interpretation accurately reflects the actual meanings of the drawn cards. Uses web search to verify card meanings. Only approves when completely satisfied.",
    instruction=prompt.VALIDATOR_INSTRUCTION,
    tools=[google_search],
    output_key="validated_reading",
)

# Step 3: Formatter Agent - Creates visually stunning presentation with ASCII art
formatter_agent = Agent(
    name="tarot_formatter",
    model="gemini-2.5-flash",
    description="Creates a visually stunning, high-quality presentation of the tarot reading with ASCII art and beautiful formatting",
    instruction=prompt.FORMATTER_INSTRUCTION,
    output_key="formatted_reading",
)

# Iterative Refinement Loop: Interpret -> Validate (repeat until approved, max 4 iterations)
interpretation_loop = LoopAgent(
    name="interpretation_loop",
    description="Iteratively refines the tarot interpretation until the validator fully approves it",
    max_iterations=4,
    sub_agents=[
        interpreter_agent,  # Create/revise interpretation
        validator_agent,    # Strictly validate accuracy
    ],
)

# Sequential Pipeline: Iterative Refinement -> Format
interpretation_pipeline = SequentialAgent(
    name="interpretation_pipeline",
    description="A sequential pipeline that iteratively interprets and validates tarot cards until approval, then creates a visually stunning formatted presentation",
    sub_agents=[
        interpretation_loop,  # Step 1: Iterative refinement (max 4 iterations)
        formatter_agent,      # Step 2: Format with ASCII art
    ],
)

# Root Agent: Orchestrates the tarot reading
root_agent = Agent(
    name="tarot_reader",
    model="gemini-2.5-flash",
    description="A professional tarot reader that draws cards and provides validated interpretations based on the Rider-Waite deck",
    instruction=prompt.ROOT_AGENT_INSTRUCTION,
    tools=[
        FunctionTool(draw_tarot_cards),
    ],
    sub_agents=[interpretation_pipeline],
)

