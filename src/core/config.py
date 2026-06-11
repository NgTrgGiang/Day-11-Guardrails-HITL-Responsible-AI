"""
Lab 11 — Configuration & API Key Setup
"""
import os
from pathlib import Path

# Load variables from a .env file at the project root (if present).
# This lets you keep OPENAI_API_KEY out of your shell and out of git.
try:
    from dotenv import load_dotenv
    _PROJECT_ROOT = Path(__file__).resolve().parents[2]
    load_dotenv(_PROJECT_ROOT / ".env")
except ImportError:
    pass  # python-dotenv not installed — fall back to real env vars


# Model identifiers
# - LLM_MODEL is passed to ADK agents via LiteLlm (note the "openai/" prefix)
# - OPENAI_MODEL is used for direct OpenAI SDK calls (attacks generator, NeMo)
LLM_MODEL = "openai/gpt-4o-mini"
OPENAI_MODEL = "gpt-4o-mini"


def setup_api_key():
    """Load OpenAI API key from environment or prompt."""
    if "OPENAI_API_KEY" not in os.environ:
        os.environ["OPENAI_API_KEY"] = input("Enter OpenAI API Key: ")
    print("API key loaded.")


# Allowed banking topics (used by topic_filter)
ALLOWED_TOPICS = [
    "banking", "account", "transaction", "transfer",
    "loan", "interest", "savings", "credit",
    "deposit", "withdrawal", "balance", "payment",
    "tai khoan", "giao dich", "tiet kiem", "lai suat",
    "chuyen tien", "the tin dung", "so du", "vay",
    "ngan hang", "atm",
]

# Blocked topics (immediate reject)
BLOCKED_TOPICS = [
    "hack", "exploit", "weapon", "drug", "illegal",
    "violence", "gambling", "bomb", "kill", "steal",
]
