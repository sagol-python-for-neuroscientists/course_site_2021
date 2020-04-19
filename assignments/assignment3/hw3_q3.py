import numpy as np


def load_data(fname: str):
    """ Load and return an '.npy' file """
    if fname.endswith(".npy"):
        return np.load(fname)


def find_in_range(data: np.ndarray, num_range=(0.3, 0.4)):
    """ Return an array containing the values of 'data' that are inside 'num_range' """
    return data[(data > num_range[0]) & (data < num_range[1])]


def first_after_val(data: np.ndarray, val=0.9):
    """ Return the position of the first value larger than val """
    return np.argwhere(data > val)[0]
