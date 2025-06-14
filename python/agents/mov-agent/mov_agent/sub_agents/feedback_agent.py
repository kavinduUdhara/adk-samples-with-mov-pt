"""Feedback agent for Movement."""
from google.adk.agents import Agent

from .. import MODEL
from . import feedback_agent_prompt

FeedbackAgent = Agent(
    model=MODEL,
    name="feedback_agent",
    description="Gather reflections and self-assessments",
    instruction=feedback_agent_prompt.PROMPT,
)
