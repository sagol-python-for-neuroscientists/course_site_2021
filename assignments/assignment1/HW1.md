# Homework Assignment, 09-03-2020

## Due date: 16-03-2020, 15:00

1. _Three consecutive double-letter words:_ Write a program that receives a word
and checks whether it has three consecutive pairs of identical letters in it.
For example:
    - `'aabbcc'` returns `True`
    - `'abccddee0123'` returns `True`
    - `'llkkbmm'` returns `False`
    - `'aaaazz'` returns `True`
    - `'bbcCdd'` returns `False`
    - The empty string `''` returns `False`

    Function signature:

    ```python
    def trifeca(word):
        """Checks whether word contains three consecutive double-letter pairs.

        Parameters
        ----------
        word : string
            Input to check

        Returns
        -------
        result : bool
            True if three consecutive double-letter pairs were found,
            False otherwise
        """
    ```

2. _Book-keeping:_ Teachers keep a record of the names of their students alongside their scores in the first and second
exams of the semester. The principal wishes to compare the grades of a single student in two different subjects, to see where students
have the highest grades.

    Write a program that compares the highest grade, for each student, in the two subjects. The program should print a "table" with the
student's name and the higher-graded subject. The table should be some data structure which is returned from the function.

    For example: In Maths, Jack received 80 in his first test and 85 in his second. In History, Jack received 75 and 95. The program
print out Jack's name alogside his better subject - History.

    ```python
    def compare_subjects_within_student(
        subj1_all_students,
        subj2_all_students
    ):
        """Compare the two subjects with their students and print out the higher-graded
        subject for each student.

        Single-subject students shouldn't be printed.

        Parameters
        ----------
        subj1_all_students, subj2_all_students
            Data structures which contain the grades of all students in a given
            subject.

        Notes
        -----
        Choice for the data structure of the function's arguments is up to you.

        Returns
        -------
        A data structure with the name of the student and the corresponding subject.
        """
    ```

    Hints:

    - Think carefully of the data structures you're using to keep the data. After you decide on it, create mock data for yourself -
    at least four students in each subject.
    - Not all students participate in all subjects. These students should be left out of the printout.

Notes:

- When functions require input, you should be the one simulating it. For example,
if a function requires a list, please submit the HW with a mock list already in place.

- Follow closely the instructions on `SubmissionGuidelines.md` - your HW is automatically checked and graded.

- If you have any Pythonic and \ or technical difficulties don't hesitate to contact me.

3. _Palindrome madness:_ A palindrome is a sequence that can be read both ways
(left to right, right to left) and have the same value, for example `1441`, or `2`.
Write a function that tests all 6 digit numbers (from 100000 to 999999, 000003 doesn't count) and finds the ones that satisfy the following conditions:
    - The number has a palindrome in its last 4 digits.
    - After adding 1, the result has a palindrome in its last 5 digts.
    - Another addition of 1 results in a palindrome in the middle 4 digits.
    - A final addition of 1 results in a 6-digit palindrome.

    The main function's signature:

    ```python
    def check_palindrome():
        """Runs through all 6-digit numbers and checks the mentioned conditions.

        The function prints out the numbers that satisfy this condition.

        Notes
        -----
        It should print out the first number (with a palindrome in its last 4 digits),
        not all four "versions" of it.
        """
    ```

    Hints:
    - You'll need at least one more function that does the actual testing.
    - The modulus operator `%` might be useful. But there are other, perhaps better options,
      to solve this question without it.

## Submission

Submission is done using the `repl.it` interface. Please [click here](https://repl.it/@hagaihargil/sagolpythonexercise1) and work inside `repl.it`. To the left you should see a `main.py` file which `import`s the others. This means that the `main.py` file uses the functions written in the other files by calling them with their proper input. Thus, your first task is to update the functions' contents in their respective files, and then run them (with some made-up inputs, if needed) from `main.py` by clicking the "Run" button. The output of the functions should be seen in the console, to the right. Also note that once you start editing the file, it should open in a new page with a different name. This new page is where you'll do your editing. Once you're done please use the "share" button, copy the "Share link" and send it over to Zvi: z.baratz@gmail.com.

Note that the submission guidelines for this exercise, as explained above, are unique to the first exercise. The other assignments will be submitted using GitHub.com, which we'll discuss in the next class.

