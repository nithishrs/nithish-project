from google.adk.agents import Agent,SequentialAgent
from google.adk.tools import google_search

sub1 = Agent(
    model='gemini-2.5-flash',
    name='sub1',
    description='A helpful assistant for user questions.',
    instruction='Check if root_agentss answers are correct',
    tools=[google_search]
)

sub2 = Agent(
    model='gemini-2.5-flash',
    name='sub2',
    description='A helpful assistant for user questions.',
    instruction='Check if root_agentss answers are correct',
    tools=[google_search]
)

# sequence= SequentialAgent(
#     name='sequence',
#     description='A helpful assistant for user questions.',
#     sub_agents=[sub1,sub2]
# )

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge, then verify using sub1',
    tools=[google_search]
)
