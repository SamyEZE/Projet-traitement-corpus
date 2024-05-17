import pandas as pd
import numpy as np
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import seaborn as sns
import json

def calculate_correlation(json_path, output_plot_path):
    # Charger les données JSON
    with open(json_path, 'r') as f:
        data = json.load(f)
    
    # Convertir en DataFrame
    df = pd.DataFrame(data)
    
    # Calculer la longueur des instructions et des réponses
    df['instruction_length'] = df['instruction'].apply(len)
    df['response_length'] = df['response'].apply(len)
    
    # Identifier les valeurs aberrantes avec un boxplot
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df[['instruction_length', 'response_length']])
    plt.title('Boxplot des longueurs des instructions et des réponses')
    plt.savefig('../plots/boxplot_lengths.png')
    
    # Calculer la corrélation de Pearson et la p-value
    correlation, p_value = pearsonr(df['instruction_length'], df['response_length'])
    print(f"Coefficient de corrélation: {correlation}")
    print(f"P-value: {p_value}")
    
    # Visualiser la corrélation
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='instruction_length', y='response_length', data=df)
    plt.title('Correlation entre la longueur des instructions et des réponses')
    plt.xlabel('Longueur des instructions')
    plt.ylabel('Longueur des réponses')
    plt.savefig(output_plot_path)
    print(f"Graphique de corrélation sauvegardé dans {output_plot_path}")

# Chemin du fichier JSON et du graphique de sortie
json_path = '../data/clean/scraped_data.json'
output_plot_path = '../plots/instruction_response_length_correlation.png'

# Exécution du script
calculate_correlation(json_path, output_plot_path)
