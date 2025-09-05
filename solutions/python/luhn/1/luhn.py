class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        if len(self.card_num.strip()) <= 1 or not all(d.isdigit() or d.isspace() for d in self.card_num):
            return False
        num = list(map(int, [d for d in self.card_num if d.isdigit()]))
        num = num[::-1]
        for d in range(1, len(num), 2):
            n = num[d] * 2
            if n > 9:
                n = n - 9
            num[d] = n
        num_sum = sum(num)
        return num_sum % 10 == 0
