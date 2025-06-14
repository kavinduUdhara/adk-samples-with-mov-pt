"""Vision agent for Movement."""
from google.adk.agents import Agent

from .. import MODEL
from . import vision_agent_prompt

VisionAgent = Agent(
    model=MODEL,
    name="vision_agent",
    description="Guide students to craft a 3–5 year vision",
    instruction=vision_agent_prompt.PROMPT,
)
