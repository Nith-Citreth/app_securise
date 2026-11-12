# Dashboard DataInsight Solutions

Application web interactive développée avec **Streamlit** pour présenter les analyses de données de l'entreprise DataInsight Solutions.

## Contexte

DataInsight Solutions souhaite moderniser la présentation de ses analyses et préparer l'arrivée de futurs modèles de Machine Learning. Ce projet propose une interface simple, accessible en ligne, versionnée avec Git et hébergée dans le cloud.

## Ce que fait l'application

- Un **menu de connexion** : les utilisateurs autorisés sont lus depuis un fichier CSV.
- Des **visualisations dynamiques** (graphiques, filtres, indicateurs) à partir des datasets de l'entreprise.
- Une interface modifiable facilement pour accueillir de futurs modèles de Machine Learning.

## Technologies utilisées

- Python
- Streamlit
- Pandas
- Plotly
- Git et GitHub
- Streamlit Community Cloud (hébergement)

## Installation (Windows)

1. Cloner le dépôt :
```powershell
git clone https://github.com/TON_PSEUDO/NOM_DU_DEPOT.git
cd NOM_DU_DEPOT
```

2. Créer l'environnement virtuel :
```powershell
python -m venv .venv
```

3. L'activer :
```powershell
.venv\Scripts\Activate.ps1
```

4. Installer les librairies :
```powershell
pip install -r requirements.txt
```

## Lancer l'application

```powershell
streamlit run app.py
```

L'application s'ouvre dans le navigateur à l'adresse `http://localhost:8501`.
Pour l'arrêter : `Ctrl+C` dans le terminal.

## Structure du projet

```
.
├── app.py              # Fichier principal de l'application
├── requirements.txt    # Liste des librairies à installer
├── .gitignore          # Fichiers exclus de Git (dont .venv)
├── utilisateurs.csv    # Utilisateurs autorisés (menu sécurisé)
└── README.md           # Ce fichier
```

## Bonnes pratiques mises en place

- **Environnement virtuel (`.venv`)** : isole les dépendances du projet.
- **`.gitignore`** : exclut le dossier `.venv` pour ne pas l'envoyer sur GitHub.
- **`requirements.txt`** : permet à n'importe qui de réinstaller les mêmes librairies.

## Déploiement

L'application est hébergée sur **Streamlit Community Cloud**, relié à ce dépôt GitHub.
À chaque `git push` sur la branche `main`, l'application se met à jour automatiquement.

Lien de l'application : https://appsecurise-nith-citreth.streamlit.app/

## Mettre à jour le projet

```powershell
git add .
git commit -m "Description du changement"
git push
```

## Auteur

Projet réalisé par *[Prénom]* dans le cadre de la formation Data Analyst.
