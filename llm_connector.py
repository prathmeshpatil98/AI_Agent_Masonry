import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Load your Google AI API key from .env
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("❌ GOOGLE_API_KEY not found in .env file!")

# Set up configuration
genai.configure(api_key=GOOGLE_API_KEY)

# Use the correct model name (e.g., gemini-pro or gemini-1.5-pro)
model = genai.GenerativeModel("gemini-1.5-pro")


def query_gemini(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error while querying Gemini: {e}"