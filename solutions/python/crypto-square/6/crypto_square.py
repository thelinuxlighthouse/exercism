'''Implement the classic method for composing secret messages called a square code.'''
import math

def cipher_text(plain_text):
    '''Implement the classic method for composing secret messages called a square code.'''
    cleaned_text = ''.join(
        char.lower()
        for char in plain_text
        if char.isalnum()
    )

    if not cleaned_text:
        return ''

    columns = math.ceil(math.sqrt(len(cleaned_text)))
    rows = math.ceil(len(cleaned_text) / columns)

    rectangle = [
        cleaned_text[index:index + columns].ljust(columns)
        for index in range(0, len(cleaned_text), columns)
    ]

    crypto_text = [
        ''.join(rectangle[row][column] for row in range(rows))
        for column in range(columns)
    ]

    return ' '.join(crypto_text)