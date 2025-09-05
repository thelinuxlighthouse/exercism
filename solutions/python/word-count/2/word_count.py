import re
from collections import Counter


def count_words(sentence):
    sentence = ' '.join(re.split(r'[\t\n,_ \.]', sentence.lower()))
    return Counter(word.strip("'") for word in re.findall(r"[\w\']+", sentence))
