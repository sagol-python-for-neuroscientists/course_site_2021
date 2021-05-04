import pathlib

import numpy as np
import pandas as pd


def largest_species(fname: pathlib.Path) -> pd.Series:
    """Returns the name of the most widespread species per year.

    Parameters
    ----------
    fname : pathlib.Path
        Filename for the columnar data containing the population numbers.

    Returns
    -------
    largest_by_year : pd.Series
        Name of most common species per year
    """
    data = pd.read_csv(fname, index_col=0, sep="\t", dtype=np.int64)
    return data.idxmax(axis=1)


def lynxes_when_hares(fname: pathlib.Path) -> pd.Series:
    """Returns the number of lynxes when hares > foxes.

    Parameters
    ----------
    fname : pathlib.Path
        Filename for the columnar data containing the population numbers.

    Returns
    -------
    lynxes : pd.Series
        Number of lynxes when hares > foxes
    """
    data = pd.read_csv(fname, index_col=0, sep="\t", dtype=np.int64)
    return data.loc[data["hare"] > data["fox"], "lynx"]


def mean_animals(fname: pathlib.Path) -> pd.DataFrame:
    """Adds a column with the normalized mean number of animals in each year.

    This means that in the year with most animals, this column will have the value of 1,
    and in the rest of the years the value will be between [0, 1).

    Parameters
    ----------
    fname : pathlib.Path
        Filename for the columnar data containing the population numbers.

    Returns
    -------
    data : pd.DataFrame
        Original dataset with the new "mean_animals" column.
    """
    data = pd.read_csv(fname, index_col=0, sep="\t", dtype=np.int64)
    # Could use the .assign() method as well
    data["mean_animals"] = data.mean(axis=1)
    min_ = data["mean_animals"].min()
    data["mean_animals"] -= min_
    data["mean_animals"] /= data["mean_animals"].max()
    return data


if __name__ == "__main__":
    fname = pathlib.Path("populations.txt")
    a = largest_species(fname)
    b = lynxes_when_hares(fname)
    d = mean_animals(fname)
