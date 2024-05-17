import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
import spacy
from collections import Counter

# Étape 2 : Calculer des statistiques de corpus
def calculate_statistics(df):
    # Calculer la longueur des textes
    df['text_length'] = df['response'].apply(len)
    
    # Calculer la longueur moyenne des textes
    average_length = df['text_length'].mean()
    print(f"Longueur moyenne des textes: {average_length}")

    # Calculer la longueur maximale des textes
    max_length = df['text_length'].max()
    print(f"Longueur maximale des textes: {max_length}")

    # Calculer la longueur minimale des textes
    min_length = df['text_length'].min()
    print(f"Longueur minimale des textes: {min_length}")

    # Calculer la distribution des longueurs des mots
    df['word_count'] = df['response'].apply(lambda x: len(x.split()))
    average_word_count = df['word_count'].mean()
    print(f"Nombre moyen de mots par réponse: {average_word_count}")

    return df, average_length, max_length, min_length, average_word_count

# Étape 5 : Calculer la loi de Zipf
def calculate_zipf_law(df, output_path):
    text = " ".join(df['response'])
    words = text.split()
    word_freq = Counter(words)
    freq_sorted = sorted(word_freq.values(), reverse=True)
    
    plt.figure(figsize=(10, 6))
    plt.plot(freq_sorted)
    plt.xscale('log')
    plt.yscale('log')
    plt.title("Loi de Zipf")
    plt.xlabel("Rang des mots")
    plt.ylabel("Fréquence des mots")
    plt.savefig(output_path)
    print(f"Graphique de la loi de Zipf sauvegardé dans {output_path}")

# Étape 3 : Visualiser les données
def visualize_data(df, output_path_prefix):
    # Visualiser la distribution des longueurs de texte
    plt.figure(figsize=(10, 6))
    sns.histplot(df['text_length'], bins=50, kde=True)
    plt.title("Distribution des longueurs de texte")
    plt.xlabel("Longueur du texte")
    plt.ylabel("Fréquence")
    plt.savefig(f"{output_path_prefix}_text_length_distribution.png")
    print(f"Graphique de distribution des longueurs de texte sauvegardé dans {output_path_prefix}_text_length_distribution.png")

    # Visualiser la distribution du nombre de mots par réponse
    plt.figure(figsize=(10, 6))
    sns.histplot(df['word_count'], bins=50, kde=True)
    plt.title("Distribution du nombre de mots par réponse")
    plt.xlabel("Nombre de mots")
    plt.ylabel("Fréquence")
    plt.savefig(f"{output_path_prefix}_word_count_distribution.png")
    print(f"Graphique de distribution du nombre de mots sauvegardé dans {output_path_prefix}_word_count_distribution.png")

# Étape 4 : Annotation avec spaCy
def annotate_data(df):
    nlp = spacy.load('en_core_web_sm')
    
    def get_entities(text):
        doc = nlp(text)
        return [(ent.text, ent.label_) for ent in doc.ents]
    
    df['entities'] = df['response'].apply(get_entities)
    return df

# Chemins des fichiers
db_path = '../data/clean/corpus.db'
output_path_prefix = '../plots/metric'

# Charger les données depuis la base de données
con = sqlite3.connect(db_path)
df = pd.read_sql_query("SELECT * FROM corpus", con)

# Exécution des étapes
df, avg_length, max_length, min_length, avg_word_count = calculate_statistics(df)
visualize_data(df, output_path_prefix)
calculate_zipf_law(df, f"{output_path_prefix}_zipf_law.png")
df = annotate_data(df)

# Sauvegarder les annotations dans un fichier JSON
df.to_json('../data/clean/annotated_data.json', orient='records', lines=True)
print("Annotation terminée et sauvegardée dans ../data/clean/annotated_data.json")

