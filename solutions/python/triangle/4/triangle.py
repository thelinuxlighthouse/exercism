def equilateral(sides):
    return len(set(sides)) == 1 and valid(sides)


def isosceles(sides):
    return len(set(sides)) < 3 and valid(sides)


def scalene(sides):
    return len(set(sides)) == 3 and valid(sides)

def valid(sides):
    sides = sorted(sides)
    return min(sides) > 0 and sum(sides[0:2]) >= sides[2]