import os
import praw
import json
import re

# Assurer que les répertoires existent
os.makedirs('../data/raw', exist_ok=True)
os.makedirs('../data/clean', exist_ok=True)

# Configuration de l'API Reddit
reddit = praw.Reddit(
    client_id='sjZrKbA3g-n1eeyVa9sIFg',
    client_secret='Nn8_vb0UPqZEnA-D3Euuwe6lji4r3w',
    user_agent='projet constitution de corpus by /u/your_username'
)

# Fonction pour catégoriser les instructions
def categorize_instruction(instruction):
    if re.search(r'how|what|why|who|when', instruction, re.IGNORECASE):
        return 'general_qa'
    elif re.search(r'give me|suggest|recommend', instruction, re.IGNORECASE):
        return 'brainstorming'
    elif re.search(r'identify|classify', instruction, re.IGNORECASE):
        return 'classification'
    elif re.search(r'known as|who is|who was', instruction, re.IGNORECASE):
        return 'information_extraction'
    else:
        return 'misc'

# Fonction pour scraper les questions, réponses et contextes de Reddit
def scrape_reddit(subreddit_name, limit=100):
    subreddit = reddit.subreddit(subreddit_name)
    posts = subreddit.hot(limit=limit)
    data = []

    for post in posts:
        if not post.stickied:
            post.comments.replace_more(limit=0)
            context = post.selftext if post.selftext else "No additional context provided."
            for comment in post.comments.list():
                if isinstance(comment, praw.models.Comment):
                    instruction = post.title
                    response = comment.body
                    category = categorize_instruction(instruction)
                    data.append({
                        'instruction': instruction,
                        'context': context,
                        'response': response,
                        'category': category
                    })
    return data

# Scraper les données du subreddit
subreddit_name = 'MachineLearning'
raw_data = scrape_reddit(subreddit_name)

# Nettoyer les données
def clean_data(data):
    clean_data = []
    for entry in data:
        clean_entry = {
            'instruction': entry['instruction'].strip(),
            'context': entry['context'].strip(),
            'response': entry['response'].strip(),
            'category': entry['category'].strip()
        }
        clean_data.append(clean_entry)
    return clean_data

cleaned_data = clean_data(raw_data)

# Sauvegarder les données brutes
with open('../data/raw/scraped_data_raw.json', 'w') as f:
    json.dump(raw_data, f, indent=4)

# Sauvegarder les données nettoyées
with open('../data/clean/scraped_data.json', 'w') as f:
    json.dump(cleaned_data, f, indent=4)

print('Données récupérées et nettoyées avec succès.')
