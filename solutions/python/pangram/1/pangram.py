def is_pangram(sentence):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    return all([l in sentence.lower() for l in letters])
