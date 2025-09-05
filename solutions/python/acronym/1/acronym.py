import re

def abbreviate(words):
    words = re.findall(r"[\da-zA-Z]+(?:\'[\da-zA-Z]+)?", words.lower())
    return ''.join(word[0].upper() for word in words)
