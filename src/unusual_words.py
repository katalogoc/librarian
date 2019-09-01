from nltk.corpus import gutenberg
from text_processing import unusual_words

print(unusual_words(gutenberg.words('carroll-alice.txt')))

