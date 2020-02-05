"""
__author__ = Hagai Har-Gil
"""


def intadd(num1, num2):
    """ Non-negative integer addition """
    if (num1 < 0) or (num2 < 0):
        raise TypeError('Input must be positive.')
    if isinstance(num1, float) or isinstance(num2, float):
        raise TypeError('Input must be integer.')

    return num1 + num2


if __name__ == '__main__':
    print(intadd(1, 2))