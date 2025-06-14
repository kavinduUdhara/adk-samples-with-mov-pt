"""Therapist agent for Movement."""
from google.adk.agents import Agent

from .. import MODEL
from . import therapist_agent_prompt

TherapistAgent = Agent(
    model=MODEL,
    name="therapist_agent",
    description="Support users when they are stressed or upset",
    instruction=therapist_agent_prompt.PROMPT,
)
