from collections import Counter


def is_isogram(string):
    allowed_chars = ['-', ' ']
    string = string.lower()
    letter_count = Counter([letter for letter in string if letter not in allowed_chars])
    return not any([value > 1 for value in letter_count.values()])