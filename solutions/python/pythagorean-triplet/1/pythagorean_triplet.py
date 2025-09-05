import math


def triplets_with_sum(number):
    pythagorean_triplet_list = []
    for b in range(number//2):
        for a in range(1, b):
            c = math.sqrt( a * a + b * b)
            if c % 1 == 0 and a+b+int(c) == number:
                pythagorean_triplet_list.append([a, b, int(c)])
    return pythagorean_triplet_list


def triplets_in_range(start, end):
    pass


def is_triplet(triplet):
    pass
