import string

plain="abcdefghijklmnopqrstuvwxyz"
cipher="zyxwvutsrqponmlkjihgfedcba"

def encode(plain_text):
    plain_text=plain_text.lower()
    encoded_text=''
    n=5
    for char in plain_text:
        if char in string.punctuation:
            continue
        if char in string.ascii_lowercase:
            encoded_text+=cipher[plain.index(char)]
        if char in string.digits:
            encoded_text+=char
    return ' '.join([encoded_text[i:i+n] for i in range(0, len(encoded_text), n)])


def decode(ciphered_text):
    ciphered_text=ciphered_text.lower()
    plain_text=''
    for char in ciphered_text:
        if char in string.punctuation or char in string.whitespace:
            continue
        if char in string.ascii_lowercase:
            plain_text+=plain[cipher.index(char)]
        if char in string.digits:
            plain_text+=char
    return plain_text
