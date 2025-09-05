class Clock:
    def __init__(self, hour, minute):
        self.hour = (hour + (minute // 60)) % 24
        self.minute = minute % 60

    def __repr__(self):
        return f"{self.hour:02}:{self.minute:02}"

    def __eq__(self, other):
        return ((self.hour * 60) + self.minute) == ((other.hour * 60) + other.minute)

    def __add__(self, minutes):
        m = self.minute + minutes
        h = self.hour + (m // 60)
        return Clock(h%24, m%60)

    def __sub__(self, minutes):
        return self.__add__(-minutes)
