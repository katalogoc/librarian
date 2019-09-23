from __future__ import division
import re
import urllib
import nltk
from nltk.corpus import brown, words, stopwords
from bs4 import BeautifulSoup

def most_close_to_style(style):
    cfd = nltk.ConditionalFreqDist(
        (genre, word)
        for genre in ['news', 'romance']
        for word in brown.words(categories=genre)
    )
    def check_words(text):
        max_frequency = 0
        most_romantic_word = None
        for word in text:
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

def get_vocabulary(text):
    return set(w.lower() for w in text if w.isalpha())

def unusual_words(text):
    vocabulary = get_vocabulary(text)
    english_vocabulary = get_vocabulary(words.words())
    unusual = vocabulary.difference(english_vocabulary)
    return sorted(unusual)

def content_fraction(text):
    sw = stopwords.words('english')
    content = [w for w in text if w.lower() not in sw]

    return len(content) / len(text)

def strip_determiners(string):
    return re.sub(r'^(a|an|the)\W|\W(a|an|the)\W', ' ', string, flags=re.IGNORECASE).strip()

def find_arithmetic_expressions(string):
    return re.findall(r'(\d+\s*(?:[+\-*/\=]\s*\d+)+)', string)

def get_raw_text_by_url(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'lxml')
    return soup.get_text()

def unknown(url):
    html = urllib.request.urlopen(url).read()
    lowercased = nltk.regexp_tokenize(str(html), r'[a-z]+')
    return unusual_words(lowercased)

def tokenize_money_dates_names_and_organizations(string):
    return nltk.regexp_tokenize(string, r'''(?x)      # set flag to allow verbose regexps
        \$\d+(?:\.|,\d+)?                             # handles monetary amounts
        | \d+(?:\.|,\d+)?%                            # handles percentage values
        | [A-Z][a-z]+                                 # handles names and organizations
    ''', gaps=False)