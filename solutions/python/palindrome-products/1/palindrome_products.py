from collections import defaultdict


def largest(min_factor, max_factor):
    return products_list(min_factor, max_factor, largest=True)


def smallest(min_factor, max_factor):
    return products_list(min_factor, max_factor)


def products_list(min_factor, max_factor, largest=False):
    if min_factor > max_factor:
        raise ValueError("Minimum factor can't be more than Maximum factor")
    products_list = [(x*y, (x, y)) for x in range(min_factor, max_factor+1) for y in range(x,max_factor+1) if str(x*y) == str(x*y)[::-1]]
    products_dict = defaultdict(list)
    if products_list:
        for value, factors in products_list:
            products_dict[value].append(factors)
        result = [(value, products_dict[value]) for value in products_dict.keys()]
        return max(result) if largest else min(result)
    return (None, [])

