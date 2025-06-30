import os

# Structure du projet LexLang
structure = {
    "lexlangM": {
        "data": {
            "lexical_list": [
                "ewé_lexical_list.csv",
                "mina_lexical_list.csv"
            ],
            "morphological_annotations": [
                "ewé_morphological_annotations.json",
                "mina_morphological_annotations.json"
            ],
            "translations": [
                "ewé_translations_fr.csv",
                "ewé_translations_en.csv",
                "mina_translations_fr.csv",
                "mina_translations_en.csv"
            ]
        },
        "models": {
            "training_data": [
                "ewé_training_data.json",
                "mina_training_data.json"
            ],
            "nlp_pipelines": [
                "spacy_pipeline.py",
                "transformers_pipeline.py"
            ]
        },
        "scripts": [
            "annotation_script.py",
            "integration_script.py"
        ],
        "docs": [
            "format.md",
            "api.md",
            "contributions.md",
            "roadmap.md"
        ],
        ".": [
            "README.md",
            "LICENSE"
        ]
    }
}

def create_structure(base_path, tree):
    for name, content in tree.items():
        current_path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(current_path, exist_ok=True)
            create_structure(current_path, content)
        elif isinstance(content, list):
            os.makedirs(base_path, exist_ok=True)
            for file in content:
                file_path = os.path.join(base_path, file)
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write("")  # fichier vide

if __name__ == "__main__":
    create_structure(".", structure)
    print("Arborescence du projet 'lexlang/' créée avec succès.")
