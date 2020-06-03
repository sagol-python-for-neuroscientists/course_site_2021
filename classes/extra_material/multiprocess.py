import multiprocessing


def add_tuple(tup):
    return tup[0] + tup[1]


def add_numbers(n1, n2):
    return n1 + n2


if __name__ == '__main__':
    tups = [(0, 1), (2, 3), (4, 5), (6, 7)]
    with multiprocessing.Pool() as pool:  # You can also enter the number of processes you wish to use
        result = pool.map(add_tuple, tups)
    print(result)

    with multiprocessing.Pool() as pool:
        result = pool.starmap(add_numbers, tups)
    print(result)
