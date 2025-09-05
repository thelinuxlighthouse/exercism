def factors(value):
    i = 2
    factors_list = []
    while value != 1:
        if value % i == 0:
            factors_list.append(i)
            value = value / i
        else:
            i += 1
    return factors_list
