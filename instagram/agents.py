from google.adk.agents import Agent, SequentialAgent
from google.adk.tools import google_search

# Sub-agent 1: Caption & hashtag validator
caption_checker = Agent(
    model="gemini-2.5-flash",
    name="caption_checker",
    description="Validates Instagram captions and hashtags",
    instruction="""
    Check if the caption is engaging, clear, and uses relevant hashtags.
    Suggest improvements if needed.
    """,
    tools=[google_search]
)

# Sub-agent 2: Best posting time checker
time_checker = Agent(
    model="gemini-2.5-flash",
    name="time_checker",
    description="Suggests best Instagram posting time",
    instruction="""
    Verify whether the suggested posting time is suitable for Instagram
    based on general engagement trends.
    """,
    tools=[google_search]
)

# Root agent: Content creator
root_agent = Agent(
    model="gemini-2.5-flash",
    name="root_agent",
    description="Instagram content creator and scheduler",
    instruction="""
    Create Instagram post ideas with:
    - Caption
    - Hashtags
    - Suggested posting time

    Then verify the output using sub agents.
    """,
    tools=[google_search]
)

# Sequential validation flow
content_validation_flow = SequentialAgent(
    name="content_validation_flow",
    description="Validates Instagram content before scheduling",
    sub_agents=[caption_checker, time_checker]
)
