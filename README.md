# 🔍 Interrogatoire - Jeu d'enquête policière

Un jeu web où vous incarnez un policier devant interroger un suspect contrôlé par une IA.

## 📋 Description

Interrogatoire est un jeu textuel où le joueur doit mener un interrogatoire pour résoudre une affaire criminelle. Le suspect, incarné par une intelligence artificielle, répondra à vos questions de manière réaliste.

## 🚀 Installation

### Prérequis

- Python 3.8+
- pip

### Étapes

```bash
# Cloner le repository
git clone <url-du-repo>

# Créer un environnement virtuel
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# ou
.venv\Scripts\activate  # Windows

# Installer les dépendances
pip install -r requirements.txt
```

## 🎮 Lancement

```bash
flask run
```

Accédez au jeu sur `http://localhost:5000`

## 📁 Structure du projet

```
├── app.py
├── requirements.txt
├── .env
├── static/
│   ├── css/
│   └── js/
├── templates/
│   └── index.html
└── README.md
```

## 📝 Licence

MIT
