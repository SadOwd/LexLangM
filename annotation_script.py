import csv
import json

def convert_csv_to_json(csv_path, json_path):
    data = []
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            data.append(row)
    with open(json_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=2, ensure_ascii=False)

# Exemple d'utilisation :
# convert_csv_to_json('data/lexical_list/ewe_lexical_list.csv', 'output.json')
