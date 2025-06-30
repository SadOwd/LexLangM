import spacy
from spacy.tokens import DocBin

def train_spacy_model(data_path):
    # Exemple de structure pour entraînement
    nlp = spacy.blank("xx")  # Langue non standard
    doc_bin = DocBin().from_disk(data_path)
    nlp.initialize()
    # Code à compléter pour entraînement réel
    return nlp
