import nltk
'''
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download()
'''
from nltk.book import *

#print (text1)
#text1.concordance("monstrous")
#text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])

def lexical_diversity(text):
    return len(set(text)) / len(text)
def percentage(count, total):
    return 100 * count / total
print (lexical_diversity(text3))
print (percentage(text4.count('a'), len(text4)))
print (FreqDist(text1))
print (FreqDist(text1).most_common(50))