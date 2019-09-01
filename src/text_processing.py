from __future__ import division
from nltk import ConditionalFreqDist
from nltk.corpus import brown

def most_close_to_style(style):
    cfd = ConditionalFreqDist(
        (genre, word)
        for genre in ['news', 'romance']
        for word in brown.words(categories=genre)
    )
    def check_words(words):
        max_frequency = 0
        most_romantic_word = None
        for word in words:
            frequency = cfd[style][word]
            if max_frequency < frequency:
                max_frequency = frequency
                most_romantic_word = word
        return most_romantic_word
    return check_words

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

def plural(word):
    if word.endswith('y'):
        return word[:-1] + 'ies'
    elif word[-1] in 'sx' or word[-2:] in ['sh', 'ch']:
        return word + 'es'
    elif word.endswith('an'):
        return word[:-2] + 'en'
    else:
        return word + 's'
