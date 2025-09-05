import string
from random import choices, seed


class Robot:

    def __init__(self):
        self.letters = string.ascii_uppercase
        self.numbers = string.digits[1:]
        self.names = set()
        self.name = self.robot_name()

    def random_name(self):
        letters = ''.join(choices(self.letters, k=2))
        numbers = ''.join(choices(self.numbers, k=3))
        name = f"{letters}{numbers}"
        return name

    def robot_name(self):
        n = self.random_name()
        if n not in self.names:
            self.names.add(n)
            return n
        else:
            seed(string.ascii_letters)
            return self.random_name()

    def reset(self):
        self.name = self.robot_name()
