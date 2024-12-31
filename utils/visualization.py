import matplotlib.pyplot as plt

def plot_word_frequency(word_counts):
    """
    Genera un gráfico de barras con la frecuencia de palabras.
    """
    words, counts = zip(*word_counts)
    plt.bar(words, counts, color='skyblue')
    plt.xlabel("Palabras")
    plt.ylabel("Frecuencia")
    plt.title("Frecuencia de palabras más comunes")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
