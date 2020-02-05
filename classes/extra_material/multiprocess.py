"""
__author__ = Hagai Har-Gil
"""
import multiprocessing


def add_tuple(tup):
    return tup[0] + tup[1]


if __name__ == '__main__':

    tups = [(0, 1), (2, 3), (4, 5), (6, 7)]
    pool = multiprocessing.Pool()  # can also enter the number of processes you wish to use
    result = pool.map(add_tuple, tups)
    print(result)
