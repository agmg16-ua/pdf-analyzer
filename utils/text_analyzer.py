import re
from collections import Counter
from langdetect import detect
from data.stopwords import STOPWORDS

def get_lang(lang):
    switch_dict = {
        "en": "english",
        "es": "spanish"
    }

    return switch_dict.get(lang, "unknown")

def select_ignored_words(lang):
    return STOPWORDS.get(get_lang(lang), set())

def tokenize_text(text):
    """
    Tokeniza el texto usando expresiones regulares.
    """
    return re.findall(r'\b\w+\b', text.lower())

def detect_language(text):
    """
    Detecta el idioma del texto.
    """
    try:
        return detect(text)
    except:
        return "unknown"

def analyze_text(text, lang='auto'):
    """
    Analiza el texto, permite el soporte multilingüe (español e inglés).
    """
    if lang == 'auto':
        lang = detect_language(text)
    
    words = tokenize_text(text)
    stop_words = select_ignored_words(lang)

    important_words = []

    for word in words:
        if word not in stop_words:
            important_words.append(word)
    
    word_count = Counter(words)
    important_word_count = Counter(important_words)
    
    return {
        "language": lang,
        "total_words": len(words),
        "most_common_words": word_count.most_common(10),
        "most_important_words": important_word_count.most_common(10),
        "num_pages": len(words) // 300  # Aproximación: 300 palabras por página
    }
