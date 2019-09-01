from nltk.corpus import reuters
from text_processing import content_fraction

print(
    'The content fraction of news about coffee is',
    content_fraction(reuters.words(categories=['coffee']))
)

print(
    'The content fraction of news about barley is',
    content_fraction(reuters.words(categories=['barley']))
)


