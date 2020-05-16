import numpy as np


def normalize_array(arr: np.ndarray) -> np.ndarray:
    """Normalizes an array to the range [0, 1].

    The maximal element will be 1 and the minimal 0, while the
    scale remains the same.

    An array containing only identical values will be returned as a zeroed array.

    Paramaters
    ----------
    arr : np.ndarray
        Input array to normalize

    Returns
    -------
    np.ndarray
        Normalized array
    """
    arr = np.nan_to_num(arr)
    arr -= arr.min()
    max_ = arr.max()
    return arr if np.isclose(max_, 0.) else arr / max_

