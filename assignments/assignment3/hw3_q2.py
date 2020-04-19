class Time:
    """
    Represents the time of the day.
    Attributes: hour, minute, second
    """
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = self._validate_input(hour, 23, 'hour')
        self.minute = self._validate_input(minute, 59, 'minute')
        self.second = self._validate_input(second, 59, 'second')

    def __str__(self):
        return f"{self.hour:02}:{self.minute:02}:{self.second:02}"  # formatting the 0's

    def _time_to_seconds(self):
        """ Convert a time to seconds """
        return self.second + self.minute * 60 + self.hour * 3600

    def is_after(self, other):
        """
        True if our time is later than the other time, False otherwise.
        Returns None if other isn't a Time instance.
        """
        if not isinstance(other, Time):
            print("Can only compare a Time instance to another one.")
            return None
        our_time = self._time_to_seconds()
        their_time = other._time_to_seconds()
        return our_time > their_time

    def _validate_input(self, val, lim, time_type):
        """
        Makes sure val is between 0 and lim, and that it's an integer.
        Returns val if it stands the checks, else 0.
        The underscore signifies an internal method
        """
        if (isinstance(val, int) and (0 <= val <= lim)):
            return val
        else:
            print(f"Value for {time_type} was inappropriate. Setting it to 0")
            return 0

    def __add__(self, other):
        """ Add two time instances, returning a new one """
        if not isinstance(other, Time):
            print("Can only add a Time instance to another one.")
            return None

        new_seconds = self.second + other.second
        new_minutes, new_seconds = divmod(new_seconds, 60)
        new_minutes += self.minute + other.minute
        new_hours, new_minutes = divmod(new_minutes, 60)
        new_hours += self.hour + other.hour
        _, new_hours = divmod(new_hours, 24)

        return Time(hour=new_hours,
                    minute=new_minutes,
                    second=new_seconds)


if __name__ == '__main__':
    t1 = Time(hour=1, minute=2, second=2)
    t2 = Time(hour=23, minute=58, second=4)
    t3 = Time(hour=24, minute=0, second=-1)

    print(f"The first time is {t1}, while the second is {t2}. What is the third? {t3}.")

    new_time = t1 + t2
    print(f"After adding the first two, we have {new_time}.")
