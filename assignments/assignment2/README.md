# Homework Assignment #2

### Date: 16-03-2020
### Due date: 30-3-2020, 15:00

This exercise's purpose is to help you familiarize yourself with some parts of the rich Python standard library. The two questions below can be solved
quite simply with existing functions that do (almost) exactly what I'm asking for, give or take some effort by you :)


## Question 1: Morse Code Interpreter

Write a program that reads a text file (`lorem.txt`), converts it to Morse code and writes it back
to a new file called `lorem_morse.txt`. In the new file, each (Morse) word should be in a new line.
**Don't loop over the string.** Rather, use [built-in Python string methods](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str) to do the _heavy lifting_.

```python
MORSE_CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
              'D': '-..',    'E': '.',      'F': '..-.',
              'G': '--.',    'H': '....',   'I': '..',
              'J': '.---',   'K': '-.-',    'L': '.-..',
              'M': '--',     'N': '-.',     'O': '---',
              'P': '.--.',   'Q': '--.-',   'R': '.-.',
              'S': '...',    'T': '-',      'U': '..-',
              'V': '...-',   'W': '.--',    'X': '-..-',
              'Y': '-.--',   'Z': '--..',

              '0': '-----',  '1': '.----',  '2': '..---',
              '3': '...--',  '4': '....-',  '5': '.....',
              '6': '-....',  '7': '--...',  '8': '---..',
              '9': '----.',

              '.': '.-.-.-', ',': '--..--', ':': '---...',
              "'": '.----.', '-': '-....-',
              }


def english_to_morse(
    input_file: str = "lorem.txt",
    output_file: str = "lorem_morse.txt"
):
    """Convert an input text file to an output Morse code file.

    Notes
    -----
    This function assumes the existence of a MORSE_CODE dictionary, containing a
    mapping between English letters and their corresponding Morse code.

    Parameters
    ----------
    input_file : str
        Path to file containing the text file to convert.
    output_file : str
        Name of output file containing the translated Morse code. Please don't change
        it since it's also hard-coded in the tests file.
    """
```

## Question 2: Spreading Virus

Pairs of people ("agents") are continuously meeting and possibly spreading a virus
they're carrying, and your job is to model the way their virus spreads.
You're given a list of agents that are about to meet in pairs, i.e. agent #1 will meet
agent #2, agent 3# with agent #4, etc. Write a program that returns the status of these
agents after each pair had their meeting.
The rules that govern this encounter are quite simple: Each agent has a name and a "category",
and the categories are:
1. Cure - a special agent that makes other agents feel better.
2. Healthy
3. Sick
4. Dying
5. Dead

Agents of categories "Healthy" and "Dead" aren't going to meet anyone - the healthy went home and
the dead are... dead. Thus, both categories should be discarded from the meetings. A "Cure" agent
improves by one step the status of other agents, that is a "Sick" agent becomes "Healthy", and a
"Dying" agent becomes "Sick". A "Cure" agent doesn't affect other "Cure" agents.

The other types of agents always worsens the conditions of other agents. When a "Sick" agent
meets a "Dying" agent the "Sick" one becomes "Dying", and the "Dying" becomes "Dead". If two
"Dying" agents meet they both become "Dead".

For the given lists of inputs write a function that takes one such list of agents, models the
"meeting" of the pairs and returns the resulting list of agents with their "categories" changed
accordingly. The returned list doesn't have to be in the same order of the original list.

Since this exercise's goal is to familiarize youselves with the Python standard library,
I've taken the liberty to model both the categories of agents and the agents themselves using
tools from the standard library:

```python
from enum import Enum
from collections import namedtuple


Type = Enum("Type", ("CURE", "HEALTHY", "SICK", "DYING", "DEAD"))
Agent = namedtuple("Agent", ("name", "category"))
```

Please read about [enumerations](https://docs.python.org/3/library/enum.html) and [namedtuple](https://docs.python.org/3/library/collections.html#collections.namedtuple)
to understand their value and use-cases.

Moreover, some key parts of this exercise can dramatically benefit from the excellent [`itertools`](https://docs.python.org/3/library/itertools.html) package.
You should review the available functions there and the given examples and see whether you can use any of them.

The signature for the main function you'll write is given below. You're encouraged to create multiple
smaller functions that this main one will use. As you'll see below, you're only measured at the output level, i.e. as long as the returned list of agents
is identical to the "true" one, your specific implementation doesn't matter.

```python
def meetup(agent_listing: tuple) -> list:
    """Model the outcome of the meetings of pairs of agents.

    The pairs of agents are ((a[0], a[1]), (a[2], a[3]), ...). If there's an uneven
    number of agents, the last agent will remain the same.

    Notes
    -----
    The rules governing the meetings were described in the question. The outgoing
    listing may change its internal ordering relative to the incoming one.

    Parameters
    ----------
    agent_listing : tuple of Agent
        A listing (tuple in this case) in which each element is of the Agent
        type, containing a 'name' field and a 'category' field, with 'category' being
        of the type Type.

    Returns
    -------
    updated_listing : list
        A list of Agents with their 'category' field changed according to the result
        of the meeting.
    """
```


## Submission

Most course assignments, including this one, will be submitted via GitHub Classroom, a special interface of GitHub which eases the creation of new, identical repositories for multiple students of the same class. Other than this convenience this repository is identical to ones you can create on your own. The submission guidelines for this exercise should also serve as a learning experience on how to work with version control and GitHub.

When you wish to answer the questions follow these steps:
1. Click the __Clone or download__ button on the top right side of this repo. Copy the link (the one ending with `.git`).
2. Open VS Code and press `Ctrl[Cmd] + Shift + P` and type `Git: Clone`. Paste the URL to the address bar and choose a folder. Click "Open Repository" to open VS Code inside that folder. This operation "cloned" the online repo and created a copy of it in your computer.
3. You may now write code, add new files and so on. Don't forget to commit your changes once in a while, normally before and after major changes, like new functions or major bug fixes. *Note:* Don't change the structure of the folder - your code files and tests should be under the same folder. You can add new files, but don't modify the names of the existing ones, otherwise the tests will fail for the wrong reasons.
4. To commit, go to the Git symbol on the left bar (fork-looking), highlight the "Changes" row and choose "Stage All Changes". Staging is a required step before committing - you'll commit evert staged changed, but you don't have to stage every change you've made. After staging, you can press the "V" icon on the top to commit the changes to the git tree. VSCode (and git) will request a message describing the changes you've made in your last commit, like "added function x" or "HW is complete". A more complete tutorial was given in class #2.
5. When you're done editing, you can push the changes to the online repo. Click the three dots (in the git fork-looking tab) and select "Push". Enter your credentials and the files should momentarily appear online.

You may push several times to the repo, we'll check the last push before the deadline by running the tests on this version and asserting that they all pass.

### Tests

In the repo you can find test classes for the questions. These classes contain unit tests, and will determine your grade for these questions. Unit tests are a very common procedure when writing code, and should be a part of any script you write. The two tests files serve as a good example of how to write these, or at least a certain type of tests. The grade for this exercise, as well as for most others, is determined completely by the success rate of the tests, meaning that if all tests pass for a given question the grade of that question is 100.

#### Running the tests

If you've heard of `pytest` and have it installed then this is the preferred way to run the tests. If you haven't, then to run them simply press the green "Run" arrow icon on the top right, which is the equivilant of writing `python test_q1.py`. The assertions at the end of the tests will fail if the condition isn't held, and so Python will raise an exception there. The code I've written under `if __name__ == '__main__'` will catch these exceptions and write them more clearly to you. When there are no more exceptions left, the file should print "Tests pass successfully."


Good luck, and don't hesitate to contact us if Google doesn't solve your technical issues :)
