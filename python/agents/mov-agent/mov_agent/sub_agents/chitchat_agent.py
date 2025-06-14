"""ChitChat agent for Movement."""
from google.adk.agents import Agent

from .. import MODEL
from . import chitchat_agent_prompt

ChitChatAgent = Agent(
    model=MODEL,
    name="chitchat_agent",
    description="Handle off-topic or motivational conversation",
    instruction=chitchat_agent_prompt.PROMPT,
)
