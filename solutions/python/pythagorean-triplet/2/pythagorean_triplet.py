import math


def triplets_with_sum(number):
    range_number = number // 2
    pythagorean_triplet_list = []
    for a in range(range_number):
        for b in range(a+1, range_number):
            c = math.sqrt( a * a + b * b)
            if c % 1 == 0 and a+b+int(c) == number:
                pythagorean_triplet_list.append([a, b, int(c)])
    return pythagorean_triplet_list


def triplets_in_range(start, end):
    pass


def is_triplet(triplet):
    pass
