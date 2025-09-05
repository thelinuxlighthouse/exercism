def is_isogram(string):
    allowed_chars = ['-', ' ']
    string = string.lower()
    letter_count = {letter: string.count(letter) for letter in set(string)}
    return False if any([(letter, count) for letter, count in letter_count.items() if count > 1 and letter not in allowed_chars]) else True
