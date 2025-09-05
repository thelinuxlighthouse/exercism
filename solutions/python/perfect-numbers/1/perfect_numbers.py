def classify(number):
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Only positive integers accepted.")
    factors = []
    # even_or_odd = True if (number % 2 == 0) else False
    for i in range(1, (number//2)+1):
        if number % i == 0:
            factors.append(i)
        else:
            continue
    if number == sum(factors):
        return "perfect"
    elif number < sum(factors):
        return "abundant"
    else:
        return "deficient"