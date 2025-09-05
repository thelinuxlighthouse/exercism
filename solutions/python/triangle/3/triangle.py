from itertools import combinations


def equilateral(sides):
    return triangle(sides, test='equilateral')


def isosceles(sides):
    return triangle(sides, test='isosceles')


def scalene(sides):
    return triangle(sides, test='scalene')


def triangle(sides, test='triangle'):
    check = {
        'equilateral': all([x == y for x, y in combinations(sides, r=2)]),
        'isosceles': any([x == y for x, y in combinations(sides, r=2)]),
        'scalene': all([x != y for x, y in combinations(sides, r=2)]),
        'triangle': all([z > 0 for z in sides]) and all([(x+y) > z for x,y in combinations(sides, r=2) for z in sides])
        }
    return check['triangle'] and check[test]