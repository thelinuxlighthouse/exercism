class Clock:
    def __init__(self, hour, minute):
        self.hour = ((hour % 24) + (minute // 60) % 24) % 24
        self.minute = minute % 60

    def __repr__(self):
        return f"{self.hour:02}:{self.minute:02}"

    def __eq__(self, other):
        return ((self.hour * 60) + self.minute) == ((other.hour * 60) + other.minute)

    def __add__(self, minutes):
        m = self.minute + minutes
        self.minute = m % 60
        h = self.hour + (m // 60)
        self.hour = h % 24
        return self.__repr__()

    def __sub__(self, minutes):
        return self.__add__(-minutes)
