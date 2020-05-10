# Homework Assignment #4

## Date: 20-04-2020
## Due date: 04-05-2020, 15:00

**Do not change the signature (definition) of the functions in the exercise.**

**Tests are run with `pytest`. It's time to learn how to use it :)**

1. _Mandelbrot Set:_

    A number is a part of the [Mandelbrot set](https://www.youtube.com/watch?v=FFftmWSzgmk) if `|z| < thresh`,
    where `z(n+1) = z(n) ** 2 + c`, `c = x + jy` is an arbitrary "2D" complex number and `n` is the index of iteration.
    Write a function that computes a 2D binary mask of the numbers that belong to the set, in the
    grid [-2, 1], [-1.5, 1.5], after `n` iterations.
    The correctness is checked qualitatively with the resulting 2D image, easily generated with `matplotlib` - an example is attached.
    Use the `extent` keyword for the `imshow` function to show image with the right boundaries.

    ```python
    def mandel(
        n: int,
        thresh: float = 50.0,
        xlims: np.ndarray = np.array([-2, 1]),
        nx: int = 1500,
        ylims: np.ndarray = np.array([-1.5, 1.5]),
        ny: int = 1500,
    ) -> np.ndarray:
        """Computes the Mandelbrot fractal on some given set of numbers.

        Parameters
        ----------
        n : int
            Number of iterations.
        thresh : float
            Threshold which decides if a number is a part of the set.
        xlims, ylims : np.ndarray
            Limits for the computation of the fractal.
        nx, ny : int
            Number of points between xlims.min() and xlims.max() to calculate the set on.

        Returns
        -------
        img : np.ndarray
            A binary image with a value of 1 if the point belongs to the set.
            The shape of the resulting image is (nx, ny).
        """
    ```

In the following two questions you should use `pandas` to solve the given
problems. Using it correctly, the resulting solution shouldn't be longer
than 3-4 lines. However, points will not be deducted for longer, convoluted,
solutions.

2. _Basic Data Manipulation:_

    The repo contains `populations.txt`, a small data file containing a table with observations
    of the number of individual animals each year.

    i. Which species has the largest population in each year? Write the following function:

    ```python
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
    ```

    The function should return a pandas Series object, each row containing the name
    of the animal with the highest population for that year.

    ii. Return a `Series` with the number of lynxes, only in the years in which
    the population of hares outgrew that of the foxes.

    ```python
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
    ```

    iii. Add a column to the `DataFrame` called `mean_animals` with the normalized mean number
    of all animals in each year. Meaning that the year with the most lynxes, hares and foxes
    combined should have a `mean_animals` value of 1, and the rest should have a value between 0 and 1.

    ```python
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
    ```

3. _More Data Munching:_

    Download the NYC 311 service requests data from [here](https://osf.io/3a6qs), and read it with pandas.

    i. What is the most common complaint? Write a function that returns a tuple
    with the complaint name and number of occasions it was reported.

    ```python
    def common_complaint(fname: pathlib.Path):
        """Finds and returns the most common complaint as (complaint_name, num).

        Parameters
        ----------
        fname : pathlib.Path
            Filename for the NYC data.

        Returns
        -------
        common_complaint : tuple
            (Complaint name, number of occasions)
        """
    ```

    ii. Which borough has the most complaints of type `Illegal Parking`?
    Return its name.

    ```python
    def parking_borough(fname: pathlib.Path) -> str:
        """Finds and returns the name of the NYC borough that has the
        most complaints of type 'Illegal Parking'.

        Parameters
        ----------
        fname : pathlib.Path
            Filename for the NYC data.

        Returns
        -------
        borough_name : str
            Name of the relevant NYC borough.
        """
    ```

    Please don't push the `.zip` (or `.csv`) file into your repository for the submission.
