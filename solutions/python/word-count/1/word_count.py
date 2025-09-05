import re
from collections import Counter


def count_words(sentence):
    sentence = ' '.join(re.split(r'[\t\n,_ \.]', sentence.lower()))
    return Counter(word[1:-1] if word.startswith('\'') and word.endswith('\'') else word for word in re.findall(r"[\w\']+", sentence))
