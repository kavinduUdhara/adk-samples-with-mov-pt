"""Data agent for Movement."""
from google.adk.agents import Agent

from .. import MODEL
from . import data_agent_prompt

DataAgent = Agent(
    model=MODEL,
    name="data_agent",
    description="Perform CRUD operations via Firebase",
    instruction=data_agent_prompt.PROMPT,
)
