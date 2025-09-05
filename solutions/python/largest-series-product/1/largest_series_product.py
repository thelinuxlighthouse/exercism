from functools import reduce
from operator import mul


def largest_product(series, size):
    if (size < 0 or any(not d.isdigit() for d in series)) or (not series and size > 0):
        raise ValueError("Something went wrong")
    elif not series or size == 0:
        return 1
    series = [int(c) for c in series]
    max_number = max(reduce(mul, seq) for seq in [series[i:i+size] for i in range(len(series)-size+1)])
    return max_number
