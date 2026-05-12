import os
import google.generativeai as genai
import ollama
from dotenv import load_dotenv


load_dotenv()
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

gemini_model = genai.GenerativeModel(
    "models/gemini-2.5-flash"
)

# -----------------------------
# LOCAL LLM (OLLAMA)
# -----------------------------
def llm_response(user_query: str) -> str:

    response = ollama.chat(
        model='phi3',
        messages=[
            {
                'role': 'user',
                'content': user_query
            }
        ]
    )

    return response['message']['content']


# -----------------------------
# GEMINI CLOUD LLM
# -----------------------------
def google_llm_response(user_query: str) -> str:

    system_prompt = (
        "You are REFLECT, an intelligent AI assistant. "
        "Answer clearly and concisely."
    )

    prompt = f"""
{system_prompt}

User: {user_query}
"""

    response = gemini_model.generate_content(prompt)

    return response.text.strip()