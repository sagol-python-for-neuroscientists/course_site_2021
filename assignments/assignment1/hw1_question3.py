"""
__author__ = Hagai Har-Gil
HW1 Question 3 Solution
"""


def is_palindrome(seq):
    """Checks whether the given sequence is equal when iterating over it
    in both directions.

    Parameters
    ----------
    seq : iterable
        Sequence to iterate over.

    Returns
    -------
    result : bool
        True if input is a palindrome, False otherwise
    """
    return seq == seq[::-1]


def check_palindrome():
    """Runs through all 6-digit numbers and checks the mentioned conditions.

    Notes
    -----
    The function prints out the numbers that satisfy this condition. It only prints
    out the first number (with a palindrome in its last 4 digits), not all four
    versions of it.
    """
    result = []
    for num in range(100000, 1000000):
        if (
            is_palindrome(str(num)[2:])
            and is_palindrome(str(num + 1)[1:])
            and is_palindrome(str(num + 2)[1:5])
            and is_palindrome(str(num + 3))
        ):
            result.append(num)
    print(result)


if __name__ == "__main__":
    print("Question 3 solution:")
    check_palindrome()
