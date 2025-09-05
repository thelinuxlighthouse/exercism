letter_values = {
    1:  'aeioulnrst',
    2:  'dg',
    3:  'bcmp',
    4:  'fhvwy',
    5:  'k',
    8:  'jx',
    10: 'qz',
}


def score(word):
    word_scores = {char: value for value in letter_values for char in letter_values[value]}
    return sum(word_scores[c] for c in word.lower())
