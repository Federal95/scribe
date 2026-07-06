from groq import Groq
from src.config import GROQ_API_KEY, STT_MODEL

client = Groq(api_key=GROQ_API_KEY)


def transcribe(audio_path: str) -> str:
    with open(audio_path, "rb") as audio_file:
        response = client.audio.transcriptions.create(
            file=audio_file,
            model=STT_MODEL,
        )

    return response.text