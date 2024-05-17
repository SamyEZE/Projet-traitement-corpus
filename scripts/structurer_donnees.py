import pandas as pd
import sqlite3

# Étape 1 : Charger et structurer les données
def structure_data(csv_path, db_path):
    # Charger les données CSV
    df = pd.read_csv(csv_path)
    
    # Connecter à la base de données SQLite
    con = sqlite3.connect(db_path)
    
    # Insérer les données dans la table SQL
    df.to_sql('corpus', con, if_exists='replace', index=False)
    
    return df, con

# Chemins des fichiers
csv_path = '../data/clean/scraped_data.csv'
db_path = '../data/clean/corpus.db'

# Exécution du script
df, con = structure_data(csv_path, db_path)
print("Données structurées et stockées dans la base de données.")
