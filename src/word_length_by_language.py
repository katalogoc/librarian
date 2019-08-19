from nltk import ConditionalFreqDist
from nltk.corpus import udhr

languages = ['English', 'German_Deutsch', 'Greenlandic_Inuktikut']

cfd = ConditionalFreqDist(
    (lang, len(word))
    for lang in languages
    for word in udhr.words(lang + '-Latin1')
)

cfd.plot(cumulative=True)
