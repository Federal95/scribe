import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("Erreur : GROQ_API_KEY absente du fichier .env")

STT_MODEL = "whisper-large-v3"

LLM_MODEL = "llama-3.3-70b-versatile"