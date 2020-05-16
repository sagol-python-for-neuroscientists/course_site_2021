import pytest

from intadd import intadd


def intadd(num1: int, num2: int) -> int:
    """Adds two numbers, assuming they're both positive integers.

    Parameters
    ----------
    num1, num2 : int
        Positive integers

    Returns
    -------
    int
        Resulting positive integer

    Raises
    ------
    ValueError
        If either number is negative
    TypeError
        If either number isn't an integer
    """
    if (not isinstance(num1, int)) or (not isinstance(num2, int)):
        raise TypeError(f"Received {num1, num2}; expected integers, not {type(num1), type(num2)}")
    if (num1 < 0) or (num2 < 0):
        raise ValueError(f"Received {num1, num2}; expected positive integers")
    return num1 + num2


standard_inputs = [(1, 2, 3), (100000, 200000, 100000 + 200000)]
@pytest.mark.parametrize('inp1, inp2, result', standard_inputs)
def test_valid_inputs(inp1, inp2, result):
    assert result == intadd(inp1, inp2)
    assert result == intadd(inp2, inp1)


negative_valueerror_inputs = [(-1, 1), (1, -2), (-2, -3)]
@pytest.mark.parametrize('inp1, inp2', negative_valueerror_inputs)
def test_negative_input_raises_valueerror(inp1, inp2):
    with pytest.raises(ValueError):
        intadd(inp1, inp2)
        intadd(inp2, inp1)


typeerror_inputs = [
    ('s', 0),
    (None, 0),
    ([], 1),
    ((), 10),
    ({}, 2),
    ({1}, 20)
]

@pytest.mark.parametrize("inp1, inp2", typeerror_inputs)
def test_invalid_input_raises_typeerror(inp1, inp2):
    with pytest.raises(TypeError):
        intadd(inp1, inp2)
        intadd(inp2, inp1)
