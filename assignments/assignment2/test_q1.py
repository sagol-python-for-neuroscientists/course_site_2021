""" Tests for question 1 - Morse code translator """
name = 'lorem_morse.txt'  # output filename, please don't change


def test_file_exists():
    with open(name) as f:
        f.read()
    assert True


def test_file_valid():
    with open(name) as f:
        data = f.read()
    assert data.count('-') == 2748
    assert data.count('.') == 4175
    assert data.count('\n') == 453


def test_individual_lines():
    with open(name) as f:
        data = f.readlines()
    assert len(data) == 454
    assert data[-1] == '.-....--.-.-..-....-.-.-'
    assert data[3].startswith('.....-')


if __name__ == "__main__":
    methods = ["test_file_exists", "test_file_valid", "test_individual_lines"]
    errors = []

    for method in methods:
        try:
            eval(method)()
        except Exception as e:
            errors.append(f"Failed when testing method 'test_{method}': {e}")
    if len(errors) > 0:
        print(errors)
    else:
        print("Tests pass successfully.")
