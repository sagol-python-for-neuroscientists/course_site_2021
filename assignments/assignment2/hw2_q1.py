"""
Solution notes:

One change I made to the MORSE_CODE dictionary is to add
the '\n' value to it, to account for the empty lines
in the original text. This helps us recreate the
text *exactly* as it was before translation to Morse.

I've also created a miniature "pipeline",
dividing each functionality into a short, clear function
which does only one thing.

Another "cool" feature shown here is the way I combine
the two dictionaries - lower case and upper case - into
one, using the ** operator.
"""
import pathlib


MORSE_CODE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    " ": "\n",
    ".": ".-.-.-",
    ",": "--..--",
    ":": "---...",
    "'": ".----.",
    "-": "-....-",
}


def english_to_morse(
    input_file: str = "lorem.txt", output_file: str = "lorem_morse.txt"
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
    file = pathlib.Path(str(input_file))
    if not file.exists():
        raise ValueError(f"File {file} doesn't exist.")
    code_ord_upper = {ord(key): val for key, val in MORSE_CODE.items()}
    code_ord_lower = {ord(key.lower()): val for key, val in MORSE_CODE.items()}
    new_code = {**code_ord_lower, **code_ord_upper}
    data = convert(file, new_code)
    to_disk(data, pathlib.Path(output_file))


def convert(file: pathlib.Path, code: dict):
    """ Convert file to one-word-in-line Morse.

    Parameters
    ----------
    file : pathlib.Path
        Filename that contains the text to convert
    code : dict
        All English alphabet as keys, Morse code as values.
        Should include the newline character '\n'

    Returns
    -------
    data : str
        A new string which is the Morse code equivalent sequence.
    """
    with open(file) as f:
        data = f.read()
    data = data.translate(code)
    return data


def to_disk(data: str, file: pathlib.Path):
    """Writes data to the disk at file's location.

    Parameters
    ----------
    data : str
        Text to write to disk
    file : pathlib.Path
        Filename location, including extension
     """
    try:
        with open(file, "w") as f:
            f.write(data)
    except PermissionError as e:
        print(f"Error: {e}. Data is still accessible in 'data' variable.")


if __name__ == "__main__":
    english_to_morse("lorem.txt")
