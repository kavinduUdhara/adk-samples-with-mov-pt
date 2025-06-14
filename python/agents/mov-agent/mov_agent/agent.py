"""Root agent for Movement demo."""
from google.adk.agents import Agent

from . import MODEL, root_agent_prompt
from .sub_agents.vision_agent import VisionAgent
from .sub_agents.goal_agent import GoalAgent
from .sub_agents.review_agent import ReviewAgent
from .sub_agents.feedback_agent import FeedbackAgent
from .sub_agents.data_agent import DataAgent
from .sub_agents.critic_agent import CriticAgent
from .sub_agents.chitchat_agent import ChitChatAgent
from .sub_agents.therapist_agent import TherapistAgent


root_agent = Agent(
    model=MODEL,
    name="mov_root_agent",
    description="Routes requests to specialized Movement agents",
    instruction=root_agent_prompt.PROMPT,
    sub_agents=[
        VisionAgent,
        GoalAgent,
        ReviewAgent,
        FeedbackAgent,
        DataAgent,
        CriticAgent,
        ChitChatAgent,
        TherapistAgent,
    ],
)
