letter_values = {
    1:  ['a', 'e', 'i', 'o', 'u', 'l', 'n', 'r', 's', 't'],
    2:  ['d', 'g'],
    3:  ['b', 'c', 'm', 'p'],
    4:  ['f', 'h', 'v', 'w', 'y'],
    5:  ['k', ],
    8:  ['j', 'x'],
    10: ['q', 'z'],
}


def score(word):
    return sum(k for k, v in letter_values.items() for c in word.lower() if c in v)
