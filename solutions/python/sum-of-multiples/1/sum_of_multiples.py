def sum_of_multiples(limit, multiples):
    return sum([i for i in range(limit) if any([x !=0 and i % x == 0 for x in multiples])])
