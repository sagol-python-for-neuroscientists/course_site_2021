import pathlib

from hw3_q1 import *


def test_using_pathlib():
    fi = FolderIterator()
    assert isinstance(fi.foldername, pathlib.Path)


def test_not_using_os_module():
    assert "os" not in dir()


def test_uniques():
    fi = FolderIterator()
    assert isinstance(fi.uniques, list)


def test_duplicates():
    fi = FolderIterator()
    assert isinstance(fi.duplicates, dict)


def test_find_unique_vals():
    fi = FolderIterator()
    fi.iter_folder()
    vals_to_find = [
        "d",
        "j",
        "q",
        "o",
        "b",
        "t",
        "f",
        "v",
        "c",
        "l",
        "a",
        "z",
        "r",
        "y",
        "e",
        "w",
        "h",
        "g",
    ]
    for item in fi.uniques:
        for val in vals_to_find:
            if val in item:
                vals_to_find.remove(val)
                break
    assert vals_to_find == []


def test_unique_keys():
    fi = FolderIterator()
    fi.iter_folder()
    keys = [
        "S2.2lL",
        "AQ.n5x",
        "rH.rbh",
        "iz.9P3",
        "jG.Roh",
        "kZ.kJo",
        "RZ.9zx",
        "DC.bQx",
        "YO.doV",
        "GZ.pVN",
        "9f.zif",
        "mU.4yL",
        "pd.k0I",
        "Rx.Pe7",
        "rj.PRj",
        "8D.blN",
        "jG.d2t",
        "kI.wOE",
    ]
    for key in fi.duplicates:
        for key_to_find in keys:
            if key_to_find in key:
                break
        else:
            assert False

    assert True


if __name__ == "__main__":
    test_functions = [
        "test_using_pathlib",
        "test_not_using_os_module",
        "test_uniques",
        "test_duplicates",
        "test_find_unique_vals",
        "test_unique_keys",
    ]
    errors = []

    for func in test_functions:
        try:
            eval(func)()
        except Exception as e:
            errors.append(f"Failed when testing method '{func}': {repr(e)}")
    if len(errors) > 0:
        print(errors)
    else:
        print("Tests pass successfully.")
