import string


class PhoneNumber:
    def __init__(self, number):
        number = ''.join([n for n in number if n in string.digits])
        if len(number) in [10, 11]:
            if len(number) == 10 and not number[:3].startswith(('0', '1')) and not number[3:6].startswith(('0', '1')):
                self.number = number
            elif len(number) == 11 and number.startswith('1') and not number[1:4].startswith(('0', '1')) and not number[4:7].startswith(('0', '1')):
                self.number = number[1:]
            else:
                raise ValueError("Wrong Number")
        else:
            raise ValueError("Wrong Number")

    @property
    def area_code(self):
        return self.number[:3]

    def pretty(self):
        return f"({self.number[:3]}) {self.number[3:6]}-{self.number[6:]}"
