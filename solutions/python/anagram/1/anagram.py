def find_anagrams(word, candidates):
    word = word.lower()
    return [w for w in candidates if ''.join(sorted(w.lower())) == ''.join(sorted(word)) and word != w.lower()]
