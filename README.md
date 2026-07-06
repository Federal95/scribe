# Scribe

Scribe est un outil de prise de notes intelligent développé en Python.

À partir d'un fichier audio, il réalise automatiquement :

1. la transcription du contenu grâce au modèle Speech-to-Text de Groq ;
2. la génération d'un compte rendu structuré grâce à un Large Language Model (LLM) de Groq ;
3. la sauvegarde du résultat au format Markdown.

Le projet a été réalisé dans le cadre du TP « Scribe : Git, GitHub et intégration d'IA serverless ».

---

# Fonctionnalités

- Transcription automatique d'un fichier audio
- Génération d'un compte rendu structuré
- Création d'un titre
- Résumé en quelques lignes
- Extraction des points clés
- Extraction des décisions et actions
- Sauvegarde automatique dans le dossier `outputs/`
- Utilisation de variables d'environnement pour sécuriser la clé API

---

# Structure du projet

```
scribe/
│
├── outputs/              # Comptes rendus générés
├── prompts/              # Prompt système du LLM
├── samples/              # Audios de test
├── src/
│   ├── config.py
│   ├── transcription.py
│   └── summary.py
│
├── main.py
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```

---

# Installation

Créer un environnement virtuel :

```bash
python -m venv .venv
```

Activer l'environnement :

Windows :

```bash
.venv\Scripts\activate
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

Créer un fichier `.env` à partir de `.env.example` puis renseigner votre clé API Groq.

Exemple :

```
GROQ_API_KEY=votre_cle_api
```

---

# Utilisation

Lancer le programme :

```bash
python main.py samples/piste.mp3
```

Le programme :

- transcrit l'audio ;
- génère un compte rendu ;
- affiche le résultat ;
- crée automatiquement un fichier Markdown daté dans `outputs/`.

---

# Technologies utilisées

- Python 3.13
- API Groq
- python-dotenv
- Git
- GitHub

---

# Modèles utilisés

## Speech-to-Text

Nous avons choisi le modèle Whisper Large V3 Turbo proposé par Groq.

Ce modèle offre :

- une excellente qualité de transcription ;
- une vitesse très élevée grâce à l'infrastructure Groq ;
- un coût réduit.

## Large Language Model

Nous avons utilisé **llama-3.3-70b-versatile**.

Ce modèle produit des résumés précis, cohérents et bien structurés tout en restant rapide.

---

# Exemple de résultat

```
# Méthode d'apprentissage de l'anglais de Michel Thomas

## Résumé

La méthode repose sur un apprentissage naturel sans mémorisation.
L'objectif est de communiquer rapidement sans stress.

## Points clés

- apprentissage progressif
- aucune mémorisation
- communication avant la grammaire

## Décisions / Actions

- écouter les enregistrements
- utiliser les pauses pour réfléchir
```

---

# Réponses aux questions

## Q1 — Pourquoi le `.gitignore` doit-il exister avant d'écrire du code manipulant des secrets ?

Le fichier `.gitignore` permet d'empêcher qu'un fichier sensible, comme `.env`, soit ajouté accidentellement à Git. Une fois une clé API publiée dans l'historique Git, il est difficile de la supprimer complètement. Il est donc préférable de protéger ces fichiers dès le début du projet.

---

## Q2 — Quels modèles STT et LLM propose Groq et lesquels avons-nous choisis ?

Pour la transcription, Groq propose notamment Whisper Large V3 et Whisper Large V3 Turbo.

Nous avons choisi **Whisper Large V3 Turbo** car il offre un excellent compromis entre qualité de transcription, rapidité d'exécution et coût.

Pour le résumé, Groq propose plusieurs modèles de langage comme Llama 3.3 ou Gemma.

Nous avons retenu **llama-3.3-70b-versatile**, capable de produire des résumés détaillés avec une très bonne qualité rédactionnelle.

---

## Q3 — Que renvoie l'API de transcription en plus du texte ?

En plus de la transcription, l'API peut également retourner :

- la langue détectée ;
- des segments de transcription ;
- les horodatages (timestamps) ;
- diverses métadonnées.

Ces informations pourraient permettre, dans une future version de Scribe, de synchroniser le texte avec l'audio ou de retrouver rapidement un passage précis.

---

## Q4 — Pourquoi avoir choisi une température de 0.2 ?

Nous avons choisi une température de **0.2** car le but est de produire un compte rendu fidèle au contenu de l'audio.

Une température faible réduit la créativité du modèle et améliore la stabilité des réponses, ce qui est préférable pour un résumé professionnel.

---

## Q5 — Quel lien entre le prompt système et les tokens en cache ?

Le prompt système est envoyé à chaque requête.

Lorsque ce prompt reste identique, certains fournisseurs peuvent mettre ses tokens en cache afin d'éviter de les retraiter intégralement. Cela améliore les performances et peut réduire le coût des appels API.

---

# Sécurité

La clé API Groq n'est jamais présente dans le dépôt Git.

Elle est stockée uniquement dans le fichier `.env`, qui est ignoré grâce au `.gitignore`.

Le fichier `.env.example` permet uniquement de documenter les variables nécessaires sans divulguer de secret.
