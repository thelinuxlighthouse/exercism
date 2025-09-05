import re
import string


class PhoneNumber:
    def __init__(self, number):
        number = ''.join([n for n in number if n in string.digits])
        if number == 11 and number.startswith('1'):
            number = number[1:]
        if not re.findall(r'^[2-9]\d{2}[2-9]\d{6}$', number):
            raise ValueError("Wrong Number")
        else:
            self.number = number

    @property
    def area_code(self):
        return self.number[:3]

    def pretty(self):
        return f"({self.number[:3]}) {self.number[3:6]}-{self.number[6:]}"
