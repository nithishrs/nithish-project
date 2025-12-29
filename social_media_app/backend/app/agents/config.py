import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    # Fallback or raise error
    print("Warning: GOOGLE_API_KEY not found in env")

genai.configure(api_key=api_key)

# Using Gemini 2.0 Flash as requested
MODEL_NAME = "gemini-2.0-flash-exp" 

def get_model():
    return genai.GenerativeModel(MODEL_NAME)
