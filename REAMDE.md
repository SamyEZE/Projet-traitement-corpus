# Outils-traitement-corpus
## TD Cours n°1

### Tâche réalisée
J'ai choisi une tâche de génération de réponses à des instructions, impliquant la création de modèles capables de répondre à divers types de questions et prompts de manière cohérente et informative.

### Corpus qui répond à cette tâche
Pour le corpus, j'ai choisi le **Databricks Dolly 15K**, qui comprend 15 000 paires prompt-réponse générées par des humains. Ce dataset est destiné à l'entraînement de modèles pour des tâches de traitement du langage naturel, comme la génération de texte, la réponse à des questions et la synthèse d'information.

Ce corpus est sous licence **CC BY-SA 3.0**, ce qui permet de l'utiliser librement tout en partageant les mêmes conditions.

### Type de prédiction
Ce corpus permet de réaliser des tâches de classification et de génération de texte, notamment pour des applications de type assistant virtuel ou chatbot.

### À quel modèle il a servi
Le Databricks Dolly 15K a été utilisé pour développer le modèle **Dolly**, un modèle de traitement du langage naturel capable de comprendre et de générer des réponses à des instructions variées.

### Constitution de mon propre corpus
Pour constituer mon propre corpus, je pourrais utiliser des méthodes similaires en collectant des données de prompt-réponse sur divers sujets via des plateformes participatives ou en utilisant des outils de génération de texte pour enrichir le dataset existant.


## TD 2 : Scraping et Structuration de Corpus

### Objectif
Constituer un corpus structuré en extrayant des données pertinentes depuis Reddit.

### Pourquoi Reddit ? 
Reddit est une plateforme idéale pour extraire des questions et réponses car elle contient de nombreuses discussions sur une variété de sujets. Les subreddits spécialisés permettent de cibler des domaines spécifiques, comme MachineLearning pour des discussions techniques et informatives. De plus, la structure des discussions Reddit facilite l'extraction de contextes et de réponses.

### Étapes Réalisées

1. **Configuration de l'API Reddit**
   - Création d'une application Reddit pour obtenir les identifiants API.
   - Configuration de `praw` pour interagir avec l'API Reddit.

2. **Scraping de Données**
   - Récupération des posts et commentaires du subreddit `MachineLearning`.
   - Extraction des instructions (questions), réponses et contextes des discussions.

3. **Catégorisation Dynamique**
   - Utilisation d'expressions régulières pour assigner des catégories aux instructions (e.g., `general_qa`, `brainstorming`, `classification`).

4. **Nettoyage et Sauvegarde des Données**
   - Nettoyage des données extraites pour supprimer les espaces superflus.
   - Sauvegarde des données brutes et nettoyées dans des fichiers JSON.
### Script Développé

Le script développé réalise les tâches suivantes :
- Configuration de l'API Reddit avec `praw`.
- Extraction des questions (instructions) et des réponses (comments) depuis Reddit.
- Ajout du contexte des discussions à partir du texte des posts.
- Catégorisation dynamique des instructions basées sur des mots-clés.
- Nettoyage des données pour supprimer les espaces et caractères superflus.
- Sauvegarde des données brutes et nettoyées dans des fichiers JSON.

### Résultats
- Un corpus structuré avec les champs `instruction`, `context`, `response` et `category`.
- Les données sont prêtes pour une analyse ou un entraînement de modèles NLP.
