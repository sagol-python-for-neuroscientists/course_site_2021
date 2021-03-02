# Submission Guidelines

(Irrelevant for execrise 1)

1. Each home assignment contains at least one question. Each question should have its own file, labeled clearly. Unless stated otherwise, all functions used to solve that specific question should be located inside that `.py` file.

2. To clarify, if a homework assignment has three questions, the submission should contain three files:
    - `hw1_question1.py`
    - `hw1_question2.py`
    - `hw1_question3.py`

    All three files should be placed in the same folder.

3. At the end of each of these `.py` file should be this unindented code block:

    ```python
    if __name__ == '__main__':
        # Question 1
        param1 = val1
        param2 = val2
        return_value = function_for_question1(param1, param2)
        print(f"Question 1 solution: {return_value}")
    ```

    * The first line checks that this file was run as the main file. If indeed so, it executes the following code block.
    * Your solution has to be run from a single function. If you wish to execute several functions\methods in your solution, do so inside this main function.
    * All needed arguments for the _single main function_, called `function_for_question1` in that case, should be defined.
    * Usually the name of this main function will be defined in the homework assignment.
    * Any returned values should be captured and printed if necessary.
    * If you wrote your script as detailed, running the answer to a question should be as easy as writing `python /path/to/hw1_question2.py` in the command line.

4. Homework (not the first) is submitted through the GitHub Classroom interface. For each homework assignment you'll receive a link to
your own private repository in GitHub, to which you'll upload ("push") the files containing the homework exercises.
At the due date, the last commit to the repository will be the one used for evaluation.
