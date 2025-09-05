from num2words import num2words


def say(number):
    if number < 0 or number > 999999999999:
        raise ValueError("Please enter a number between 0 and 999999999999")
    return ' '.join(' '.join([word.strip() for word in num2words(number).split(',')]).split(' and '))
