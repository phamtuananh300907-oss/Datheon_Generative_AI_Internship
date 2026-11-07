# Connect Python to Gemini API through SDK google_genai, read from .env:

import os
from dotenv import load_dotenv
from google import genai
from dotenv import load_dotenv

load_dotenv()

def get_genai_client() -> genai.Client:
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key or api_key.strip() == "" or api_key == "your_api_key_here":
        raise ValueError("API key is required")

    return genai.Client(api_key=api_key)