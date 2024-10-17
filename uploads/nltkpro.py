import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
nltk.download('punkt')
nltk.download('punkt_tab')

def analyze_text(text):
    sentences = sent_tokenize(text)
    print("Segmented Sentences:")
    for i, sentence in enumerate(sentences):
        print(f"{i + 1}: {sentence}")

    print("\nTokenized Words:")
    for i, sentence in enumerate(sentences):
        words = word_tokenize(sentence)
        print(f"{i + 1}: {words}")

text = "The cat is on the mat. It is sunny today. Let's go for a walk."
analyze_text(text)
