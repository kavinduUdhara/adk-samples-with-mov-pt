"""Initialization for mov-agent."""
import os

MODEL = os.getenv("GOOGLE_GENAI_MODEL", "gemini-2.0-pro")

from . import agent  # noqa: E402  # pylint: disable=wrong-import-position
