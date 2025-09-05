def is_armstrong_number(number):
    power = len(str(number))
    digits_sum = sum([int(n)**power for n in str(number)])
    return digits_sum == number or False
