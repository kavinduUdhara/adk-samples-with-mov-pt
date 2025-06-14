"""Review agent for Movement."""
from google.adk.agents import Agent

from .. import MODEL
from . import review_agent_prompt

ReviewAgent = Agent(
    model=MODEL,
    name="review_agent",
    description="Lead active recall sessions on tasks",
    instruction=review_agent_prompt.PROMPT,
)
