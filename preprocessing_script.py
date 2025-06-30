import re
import unicodedata

def normalize_unicode(text):
    """
    Normalise les caractères accentués (NFC → NFD) et supprime les diacritiques inutiles.
    """
    text_nfkd = unicodedata.normalize('NFKD', text)
    return ''.join([c for c in text_nfkd if not unicodedata.combining(c)])

def basic_cleaning(text):
    """
    Nettoyage de base : minuscules, suppression des ponctuations inutiles.
    """
    text = text.lower()
    text = re.sub(r"[!?.,;:«»\"\']", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def tokenize_text(text):
    """
    Tokeniseur simple basé sur les espaces — à adapter plus tard aux règles éwé/mina.
    """
    return text.split()

def preprocess(text):
    """
    Étapes complètes de prétraitement : normalisation, nettoyage, tokenisation.
    """
    text = normalize_unicode(text)
    text = basic_cleaning(text)
    tokens = tokenize_text(text)
    return tokens

# Exemple d'utilisation
if __name__ == "__main__":
    phrases = [
        "Ámɛ dɔ nyuie! (Très bien fait.)",
        "Abɔ ga nɔvi ; eƒe yé wò."
    ]

    for phrase in phrases:
        print(f"Original: {phrase}")
        print(f"Prétraité: {preprocess(phrase)}\n")
