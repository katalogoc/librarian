from nltk import corpus, ConditionalFreqDist
from src.take import take


cfd = ConditionalFreqDist(
    (genre, word)
    for genre in take(corpus.brown.categories(), 5)
    for word in corpus.brown.words(categories='news')
)

cfd.plot()
