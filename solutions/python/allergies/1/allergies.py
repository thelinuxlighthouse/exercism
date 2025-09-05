class Allergies:

    def __init__(self, score):
        self.score = score
        self.items_value = {
            'eggs': 1,
            'peanuts': 2,
            'shellfish': 4,
            'strawberries': 8,
            'tomatoes': 16,
            'chocolate': 32,
            'pollen': 64,
            'cats': 128,
        }

    def allergic_to(self, item):
        return self.score & self.items_value[item] != 0

    @property
    def lst(self):
        return [allergic for allergic in self.items_value.keys() if self.allergic_to(allergic)]
