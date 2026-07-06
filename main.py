import sys
from pathlib import Path
from datetime import datetime

from src.transcription import transcribe
from src.summary import summarize


def main():
    if len(sys.argv) != 2:
        print("Usage : python main.py <audio>")
        return

    audio = sys.argv[1]

    print("Transcription...")
    texte = transcribe(audio)

    print("Résumé...")
    resume = summarize(texte)

    print("\n===== RÉSULTAT =====\n")
    print(resume)

    Path("outputs").mkdir(exist_ok=True)

    nom = datetime.now().strftime("%Y%m%d_%H%M%S.md")

    with open(Path("outputs") / nom, "w", encoding="utf-8") as f:
        f.write(resume)

    print(f"\nCompte rendu sauvegardé dans outputs/{nom}")


if __name__ == "__main__":
    main()