"""Goal agent for Movement."""
from google.adk.agents import Agent

from .. import MODEL
from . import goal_agent_prompt

GoalAgent = Agent(
    model=MODEL,
    name="goal_agent",
    description="Create goals and tasks from the student's vision",
    instruction=goal_agent_prompt.PROMPT,
)
