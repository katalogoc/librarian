from nltk import ConditionalFreqDist
from nltk.corpus import brown

categories = [
    'news',
    'romance'
]

cfd = ConditionalFreqDist(
    (genre, word)
    for genre in categories
    for word in brown.words(categories=genre)
    if (len(word) > 6)
)

print('The most used word in news is', cfd['news'].max())

print('The most used word in romance is', cfd['romance'].max())
