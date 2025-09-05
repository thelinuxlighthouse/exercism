import re
import string

def is_valid(isbn):
    digits = list(string.digits) + ['10']
    if isbn and isbn[-1] == 'X':
        isbn = list(isbn[:-1]) + ['10']
    isbn = [n for n in isbn if n in digits]
    if len(isbn) == 10:
        return True if sum([(int(i) * x) for i, x in zip(isbn, range(10, 0, -1))]) % 11 == 0 else False
    return False

