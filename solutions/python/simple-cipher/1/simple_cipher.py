import secrets
from itertools import cycle
from string import ascii_lowercase



class Cipher:
    def __init__(self, key=None):
        if not key:
            key = ''.join(secrets.choice(ascii_lowercase) for i in range(100))
        self.key = key

    def encode(self, text):
        text = text.lower()
        return ''.join(ascii_lowercase[(ascii_lowercase.index(letter) + ascii_lowercase.index(subst)) % 26]
                       for letter, subst in zip(text, cycle(self.key)))

    def decode(self, text):
        text = text.lower()
        return ''.join(ascii_lowercase[(ascii_lowercase.index(letter) - ascii_lowercase.index(subst)) % 26]
                       for letter, subst in zip(text, cycle(self.key)))
