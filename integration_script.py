import json

def load_lexicon(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def search_word(lexicon, word):
    return [entry for entry in lexicon if entry['mot'] == word]

# Exemple :
# lexicon = load_lexicon('data/morphological_annotations/ewe_morphological_annotations.json')
# print(search_word(lexicon, 'dɔ'))
