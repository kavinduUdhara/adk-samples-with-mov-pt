"""Critic agent for Movement."""
from google.adk.agents import Agent

from .. import MODEL
from . import critic_agent_prompt

CriticAgent = Agent(
    model=MODEL,
    name="critic_agent",
    description="Validate plans for feasibility",
    instruction=critic_agent_prompt.PROMPT,
)
