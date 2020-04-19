# Homework Assignment #3

## Date: 30-03-2020

## Due date: 13-04-2019, 15:00

1. _Duplicates Discovery:_
Define a class that scans through a folder with all of its subfolders and returns the following:

* Names and content of the unique files. "Unique" in this sense means, that if two files - `a.txt` and `b.tif` for example -
have the same content, only the first file - i.e. higher up the folder hierarchy - should be included in this "uniques" list, while the second (`b.tif`) can be discarded.
* Names of the "parent" files and their duplicates, held together in a dictionary. In the example above, the parent file
is `a.txt`, since it was first in line, and its duplicate is `b.tif`. If another file with the same content as `a.txt` and `b.tif`
will be found it will be added to that dictionary under `a.txt` again.

Note: Please use the `pathlib` module we showed in class, and not the `os` module.

```python
class FolderIterator:
    """Iterates through the supplied folder, finding duplicates.

    Call the iter_folder() method to parse the directory.

    Attributes
    ----------
    foldername : path-like
        Name of base folder to iterate on.
    uniques : list
        A list of unique files in the folder and their content.
    duplicates : dict
        The keys are the parent files and the values are a list of filenames
        with the same content.
    """
    def __init__(self, foldername='./base'):
        self.foldername = ...  # pathlib.Path instance
        self.uniques = ...  # list instance
        self.duplicates = ...  # dict instance
        # Other attributes may follow

    def iter_folder(self):
        """Main function to find duplicate and unique files in the filesystem."""
        pass

```

The folder in question is `base`, also located in this repo.

2. _The Time Class:_
    * Define the `Time` class:

    ```python
    class Time:
        """
        Represents the time of the day.
        Attributes: hour, minute, second
        """
    ```

    * Give default values to the `__init__` function.
    * Validate that the input fits a 24 hour clock. Think of as many edge-cases as you can. If the input
    isn't valid reset that value to 0.
    * Override the `__str__` method so that when you print a Time instance it prints out nicely.
    * Define a `Time().is_after(other_time)` method. that returns `True` if the first `Time()` is later
    than the `other_time` instance, and `False` otherwise. `00:00:00` is the earliest, `23:59:59` is the latest.
    * Overload the `__add__` operator to allow the addition of two `Time` instances.
        - Make sure you deal with all possible cases - "overflow" of minutes
        and seconds, and that after `23:59:59` comes `00:00:00`.


3. _Basic `numpy` Calculations:_

    Saving and loading `numpy` arrays is done using the functions `np.load`, `np.save` and `np.savez`. A single array is saved in the `.npy` format using `np.save`, while a dictionary of arrays is saved to the `.npz` format using `np.savez`. Both data structures can be read using `np.load`. In the repo you can see `data.npy`, a single 4D array that I randomly generated. The file `hw3_q3.py` should contain functions that take this specific array as input.

    i. Define the `load_data` function which receives a filename and returns the array.

    ```python
    def load_data(fname: str):
        """ Load and return an '.npy' file """
    ```

    ii. Find and return all numbers within the range (0.3, 0.4) in the array. Note: exclusive on both ends.

    ```python
    def find_in_range(data: np.ndarray, num_range: tuple=(0.3, 0.4)):
        """ Return an array containing the values of 'data' that are inside 'num_range' """
    ```

    iii. Return the index of the first value larger than 0.9, the input value. The index is a
    `numpy` array with one dimension and four values, which are the coordinates at which one can find
    this value.
    
    ```python
    def first_after_val(data: np.ndarray, val: float=0.9) -> np.ndarray:
        """ Return the position of the first value larger than val """
    ```

## Tests

The tests for both questions are provided. Again, assignment grading is mostly based on the success
of the tests, for all three questions. I do reserve myself the right to lower (or raise) the grade under
some circumstances.
