from utils.pdf_processor import extract_text_from_pdf
from utils.text_analyzer import analyze_text
from utils.visualization import plot_word_frequency

def main():
    pdf_path = "file/documento.pdf"  # Ruta del PDF
    text = extract_text_from_pdf(pdf_path)  # Extraer texto del PDF
    stats = analyze_text(text)  # Analizar texto
    
    # Imprimir estadísticas
    print(f"Número de páginas: {stats['num_pages']}")
    print(f"Idioma detectado: {stats['language']}")
    print(f"Palabras más comunes: {stats['most_common_words']}")
    print(f"Palabras más importantes: {stats['most_important_words']}")
    
    # Visualizar resultados
    plot_word_frequency(stats["most_important_words"])

if __name__ == "__main__":
    main()
