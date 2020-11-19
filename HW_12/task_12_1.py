class MyTime:
    def __init__(self, hours=0, minutes=0, seconds=0, time_str=None, other=None):
        if other:
            self.hours = other.hours
            self.minutes = other.minutes
            self.seconds = other.seconds
        elif time_str:
            val = time_str.split(':')
            self.hours = int(val[0])
            self.minutes = int(val[1])
            self.seconds = int(val[2])
            self.total_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds
        else:
            self.hours = hours
            self.minutes = minutes
            self.seconds = seconds
            self.total_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds

    # =
    def __eq__(self, other):
        return (
                self.hours == other.hours and
                self.minutes == other.minutes and
                self.seconds == other.seconds
        )

    # !=
    def __ne__(self, other):
        return (
                self.hours != other.hours or
                self.minutes != other.minutes or
                self.seconds != other.seconds
        )

    # <
    def __lt__(self, other):
        o_time = other.hours * 3600 + other.minutes * 60 + other.seconds
        return self.total_seconds < o_time

    # >
    def __gt__(self, other):
        o_time = other.hours * 3600 + other.minutes * 60 + other.seconds
        return self.total_seconds > o_time

    # <=
    def __le__(self, other):
        o_time = other.hours * 3600 + other.minutes * 60 + other.seconds
        return self.total_seconds <= o_time

    # >=
    def __ge__(self, other):
        o_time = other.hours * 3600 + other.minutes * 60 + other.seconds
        return self.total_seconds >= o_time

    # +
    def __add__(self, other):
        seconds = self.seconds + other.seconds
        minutes = self.minutes + other.minutes + seconds // 60
        seconds %= 60
        hours = (self.hours + other.hours) % 24 + minutes // 60
        minutes %= 60
        return MyTime(hours, minutes, seconds)

    # -
    def __sub__(self, other):
        o_time = other.hours * 3600 + other.minutes * 60 + other.seconds
        my_time = self.total_seconds - o_time
        if my_time < 0:
            my_time = 86400 - abs(my_time)
            hours = my_time // 3600
            minutes = my_time % 3600 // 60
            seconds = my_time % 60
        else:
            hours = my_time // 3600
            minutes = my_time % 3600 // 60
            seconds = my_time % 60
        return MyTime(hours, minutes, seconds)

    # * on number
    def __mul__(self, other):
        my_time = self.total_seconds * other
        hours = my_time // 3600 % 24
        minutes = my_time % 3600 // 60
        seconds = my_time % 60
        return MyTime(hours, minutes, seconds)

    # show time
    def __str__(self):
        return f'{self.hours}:{self.minutes}:{self.seconds}'
