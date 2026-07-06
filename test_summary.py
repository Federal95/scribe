from src.transcription import transcribe
from src.summary import summarize

texte = transcribe("samples/piste.mp3")

resume = summarize(texte)

print("\n===== TRANSCRIPTION =====\n")
print(texte)

print("\n===== RÉSUMÉ =====\n")
print(resume)