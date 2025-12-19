"""Social Media Campaign Manager - A parallel multi-agent system that posts to multiple social platforms simultaneously.

This demonstrates how to run multiple agents in parallel, where each agent works
independently on different aspects of a task simultaneously.
"""

from google.adk.agents import Agent, SequentialAgent, ParallelAgent

from . import prompt

# Twitter/X Pipeline: Draft -> Post
twitter_agent = SequentialAgent(
    name="twitter_agent",
    description="Drafts and posts a tweet to Twitter/X",
    sub_agents=[
        Agent(
            name="twitter_drafter",
            model="gemini-2.5-flash",
            instruction=prompt.TWITTER_DRAFTER_INSTRUCTION,
            output_key="drafted_tweet",
        ),
        Agent(
            name="twitter_publisher",
            model="gemini-2.5-flash",
            instruction=prompt.TWITTER_PUBLISHER_INSTRUCTION,
            output_key="twitter_result",
        ),
    ],
)

# LinkedIn Pipeline: Draft -> Post
linkedin_agent = SequentialAgent(
    name="linkedin_agent",
    description="Drafts and posts content to LinkedIn",
    sub_agents=[
        Agent(
            name="linkedin_drafter",
            model="gemini-2.5-flash",
            instruction=prompt.LINKEDIN_DRAFTER_INSTRUCTION,
            output_key="drafted_linkedin_post",
        ),
        Agent(
            name="linkedin_publisher",
            model="gemini-2.5-flash",
            instruction=prompt.LINKEDIN_PUBLISHER_INSTRUCTION,
            output_key="linkedin_result",
        ),
    ],
)

# Instagram Pipeline: Draft -> Post
instagram_agent = SequentialAgent(
    name="instagram_agent",
    description="Drafts and posts content to Instagram",
    sub_agents=[
        Agent(
            name="instagram_drafter",
            model="gemini-2.5-flash",
            instruction=prompt.INSTAGRAM_DRAFTER_INSTRUCTION,
            output_key="drafted_instagram_post",
        ),
        Agent(
            name="instagram_publisher",
            model="gemini-2.5-flash",
            instruction=prompt.INSTAGRAM_PUBLISHER_INSTRUCTION,
            output_key="instagram_result",
        ),
    ],
)

# Parallel Social Media Campaign: All three platforms run simultaneously
social_campaign_agent = ParallelAgent(
    name="social_campaign_agent",
    description="Posts content to Twitter, LinkedIn, and Instagram simultaneously in parallel",
    sub_agents=[
        twitter_agent,    # Twitter/X channel
        linkedin_agent,  # LinkedIn channel
        instagram_agent, # Instagram channel
    ],
)

# Campaign Summary Agent: Summarizes the results
campaign_summary_agent = Agent(
    name="campaign_summary_agent",
    model="gemini-2.5-flash",
    description="Summarizes the results of the parallel social media campaign",
    instruction=prompt.CAMPAIGN_SUMMARY_INSTRUCTION,
)

# Main Pipeline: Post to all platforms in parallel, then summarize
social_campaign_pipeline = SequentialAgent(
    name="social_campaign_pipeline",
    description="Posts to all social platforms in parallel, then summarizes campaign results",
    sub_agents=[
        social_campaign_agent,  # Parallel posting
        campaign_summary_agent,  # Summary of results
    ],
)

# Root Agent: Orchestrates the entire social media campaign
root_agent = Agent(
    name="social_media_campaign_manager",
    model="gemini-2.5-flash",
    description="A multi-agent system that manages social media campaigns by posting to Twitter, LinkedIn, and Instagram simultaneously",
    instruction=prompt.ROOT_AGENT_INSTRUCTION,
    sub_agents=[social_campaign_pipeline],
)

