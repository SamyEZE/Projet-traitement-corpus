import json
import pandas as pd
from sklearn.model_selection import train_test_split

# Charger les données nettoyées
with open('../data/clean/scraped_data.json', 'r') as f:
    data = json.load(f)

# Convertir les données en DataFrame
df = pd.DataFrame(data)

# Diviser les données en train et test
train, test = train_test_split(df, test_size=0.2, random_state=42)

# Sauvegarder les jeux de données train et test en JSON
train.to_json('../data/clean/scraped_data_train.json', orient='records', lines=True)
test.to_json('../data/clean/scraped_data_test.json', orient='records', lines=True)

print("Les jeux de données ont été divisés et sauvegardés avec succès.")


