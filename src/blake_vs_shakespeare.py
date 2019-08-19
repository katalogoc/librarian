from __future__ import division
from nltk.corpus import gutenberg
from most_diverse_text import most_diverse

macbeth = gutenberg.words('shakespeare-macbeth.txt')

blake_poems = gutenberg.words('blake-poems.txt')

most_diverse([macbeth, blake_poems])

print(most_diverse([macbeth, blake_poems]))
