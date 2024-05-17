import pandas as pd
import json

# Charger les données nettoyées
with open('../data/clean/scraped_data.json', 'r') as file:
    data = json.load(file)

# Convertir en DataFrame pandas
df = pd.DataFrame(data)

# Sauvegarder au format CSV
df.to_csv('../data/clean/scraped_data.csv', index=False)

# Sauvegarder au format JSON (jsonlines)
df.to_json('../data/clean/scraped_data_lines.json', orient='records', lines=True)

print("Données sauvegardées au format CSV et JSON.")
