"""
__author__ = Hagai Har-Gil
HW1 Question 1 Solution

This is by far not the fastest solution, but I wanted to show
you how I divide the question into a main function (trifeca)
and a smaller function (_three_pairs_in_a_row) that does the "heavy
lifting".
"""


def trifeca(word):
    """Checks whether word contains three consecutive double-letter pairs.

    Parameters
    ----------

    word : string
        Word to check the condition

    Returns
    -------
    value : bool
        True if input contained three consecutive double-letter pairs,
        False otherwise.
    """
    if len(word) < 6:
        return False

    first_letters = word[::2]
    second_letters = word[1::2]
    # Deal with pairs starting in an even letter
    if _three_pairs_in_a_row(first_letters, second_letters):
        return True
    # If we reached here we need to deal with the case of a pair of letters
    # starting in an odd letter
    else:
        return _three_pairs_in_a_row(first_letters[1:], second_letters)


def _three_pairs_in_a_row(firsts, seconds):
    """Iterate over pairs of letters, counting the number of consecutrive
    pairs and returning True if we have three in a row.

    Parameters
    ----------
    firsts, seconds : str
        Strings to iterate and compare over.

    Returns
    -------
    value : bool
        True if input contained three consecutive double-letter pairs,
        False otherwise.
    """
    num_pairs = 0
    for first, second in zip(firsts, seconds):
        if first == second:
            num_pairs += 1
            if num_pairs == 3:
                return True
        else:
            num_pairs = 0
    return False


# This block is used to run code from the command line \ via the green
# 'run' arrow. More on that later.
if __name__ == "__main__":
    print("Question 1 solution:")
    strings = ["aabbcc", "llkkbmm", "434343", "abccddee0123", "aaaazz", "bbcCdd", ""]
    ground_truth = [True, False, False, True, True, False, False]
    for string, truth in zip(strings, ground_truth):
        print(
            f"For the string {string}, my function returned {trifeca(string)}, "
            f"while the real answer is {truth}."
        )

