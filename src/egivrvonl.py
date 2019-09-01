from nltk import FreqDist
from nltk.corpus import words

puzzle_letters = FreqDist('egivrvonl')

obligatory = 'r'

wordlist = words.words()

result = [w for w in wordlist if len(w) > 5 and obligatory in w and FreqDist(w) <= puzzle_letters]

print(result)
