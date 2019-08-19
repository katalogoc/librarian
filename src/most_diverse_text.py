from __future__ import division

def lexical_diversity(text):
    return len(text) / len(set(text))

def most_diverse(texts):
    most_diverse_text = None

    max_diversity = 0

    for text in texts:
        diversity = lexical_diversity(text)

        if diversity > max_diversity:
            most_diverse_text = text

    return most_diverse_text
