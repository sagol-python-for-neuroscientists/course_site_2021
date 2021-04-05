from hw3_q2 import *


class TestTime:
    """
    Unit tests for the Time question. If no errors pop
    during the execution, and the summary printout doesn't
    contain any errors, your grade for the question will be perfect.
    """

    def test_existence(self):
        assert Time(hour=0, minute=0, second=0)

    def test_negative_input(self):
        t = -1
        time = Time(t, t, t)
        assert not time.hour == t or time.minute == t or time.second == t

    def test_string_input(self):
        t = "a"
        time = Time(t, t, t)
        assert not time.hour == t or time.minute == t or time.second == t

    def test_too_high_input(self):
        t = 300
        time = Time(t, t, t)
        assert not time.hour == t or time.minute == t or time.second == t

    def test_float_input(self):
        t = 22.9
        time = Time(t, t, t)
        assert not time.hour == t or time.minute == t or time.second == t

    def test_seconds_input(self):
        time = Time(second=61)
        assert time.second <= 59

    def test_minutes_input(self):
        time = Time(minute=61)
        assert time.minute <= 59

    def test_hours_input(self):
        time = Time(hour=78)
        assert time.hour <= 23

    def test_true_is_after(self):
        time = Time(0, 0, 0)
        time2 = Time(0, 0, 1)
        assert time2.is_after(time)

    def test_false_is_after(self):
        time = Time(0, 0, 0)
        time2 = Time(0, 0, 1)
        assert not time.is_after(time2)

    def test_same_time(self):
        time = Time(0, 0, 0)
        time2 = Time(0, 0, 0)
        assert not time2.is_after(time)

    def test_hours_after(self):
        time = Time(1, 59, 59)
        time2 = Time(2, 0, 0)
        assert time2.is_after(time)

    def test_minutes_after(self):
        time = Time(22, 22, 22)
        time2 = Time(22, 23, 0)
        assert time2.is_after(time)

    def test_allowed_addition(self):
        time = Time(0, 0, 0)
        time2 = Time(1, 1, 1)
        time3 = time + time2
        assert time3.second == 1 and time3.minute == 1 and time3.hour == 1

    def test_allowed_addition_2(self):
        time = Time(10, 10, 10)
        time2 = Time(3, 4, 5)
        time3 = time + time2
        assert time3.second == 15 and time3.minute == 14 and time3.hour == 13

    def test_seconds_overflow(self):
        time = Time(0, 0, 20)
        time2 = Time(0, 0, 40)
        time3 = time + time2
        assert time3.second == 0

    def test_seconds_double_overflow(self):
        time = Time(0, 0, 50)
        time2 = Time(1, 1, 50)
        time3 = time + time2 + time2
        assert time3.second == 30 and time3.minute == 4 and time3.hour == 2

    def test_minutes_overflow(self):
        time = Time(0, 40, 0)
        time2 = Time(0, 30, 40)
        time3 = time + time2
        assert time3.second == 40 and time3.minute == 10 and time3.hour == 1

    def test_hours_overflow(self):
        time = Time(23, 1, 1)
        time2 = Time(1, 0, 0)
        time3 = time + time2
        assert time3.second == 1 and time3.minute == 1 and time3.hour == 0

    def test_hours_overflow_with_seconds(self):
        time = Time(23, 59, 3)
        time2 = Time(0, 0, 59)
        time3 = time + time2
        assert time3.second == 2 and time3.minute == 0 and time3.hour == 0


if __name__ == "__main__":
    ttests = TestTime()
    methods = [
        "existence",
        "negative_input",
        "string_input",
        "too_high_input",
        "float_input",
        "seconds_input",
        "minutes_input",
        "hours_input",
        "true_is_after",
        "false_is_after",
        "same_time",
        "hours_after",
        "minutes_after",
        "allowed_addition",
        "allowed_addition_2",
        "seconds_overflow",
        "seconds_double_overflow",
        "minutes_overflow",
        "hours_overflow",
        "hours_overflow_with_seconds",
    ]
    errors = []

    for method in methods:
        try:
            getattr(ttests, "test_" + method)()
        except AssertionError as e:
            errors.append(f"Failed when testing method 'test_{method}': {e}")

    if len(errors) > 0:
        print(errors)
    else:
        print("Tests pass successfully.")
