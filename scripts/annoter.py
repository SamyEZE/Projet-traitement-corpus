import pandas as pd
import spacy

# Charger les données CSV et JSON
df_csv = pd.read_csv('../data/clean/scraped_data.csv')
df_json = pd.read_json('../data/clean/scraped_data_lines.json', lines=True)

# Charger le modèle de langue anglaise de spaCy
nlp = spacy.load('en_core_web_sm')

# Fonction pour annoter les réponses avec spaCy
def annotate_responses(df):
    annotations = []
    for entry in df.itertuples():
        doc = nlp(entry.response)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        annotations.append({
            'instruction': entry.instruction,
            'context': entry.context,
            'response': entry.response,
            'category': entry.category,
            'entities': entities
        })
    return annotations

# Annoter les données JSON
annotated_data = annotate_responses(df_json)

# Afficher quelques exemples annotés
for item in annotated_data[:5]:
    print(f"Instruction: {item['instruction']}")
    print("Entités nommées dans la réponse:")
    for ent in item['entities']:
        print(f"{ent[0]} - {ent[1]}")
    print("\n")

# Optionnel : sauvegarder les annotations dans un fichier JSON
import json
with open('../data/clean/annotated_data.json', 'w') as f:
    json.dump(annotated_data, f, indent=4)

print("Annotation terminée et sauvegardée dans ../data/clean/annotated_data.json")
