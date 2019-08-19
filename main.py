from __future__ import division
from nltk.corpus import gutenberg

# print(gutenberg.fileids())

macbeth = gutenberg.words('shakespeare-macbeth.txt')

blake_poems = gutenberg.words('blake-poems.txt')

def lexical_diversity(text):
    return len(text) / len(set(text))

def most_diverse(texts):
    most_diverse_text = None

    max_diversity = 0

    for text in texts:
        diversity = lexical_diversity(text)

        if (diversity > max_diversity):
            most_diverse_text = text

    return most_diverse_text


print(most_diverse([macbeth, blake_poems]))