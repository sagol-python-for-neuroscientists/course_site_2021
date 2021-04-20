import pathlib


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
    # Since we defined self.foldername to be a pathlib.Path object,
    # recursive iteration in that folder is very clear and easy.
    # The content of the unique files is held in the "uniques"
    # attribute, which is a list in which each element is a tuple
    # consisting of the filename and its content. A more elaborate
    # solution might have used collections.namedtuple, another
    # dictionary or a small class desgined to hold this type of
    # data.

    def __init__(self, foldername="./base"):
        self.foldername = pathlib.Path(str(foldername))
        assert self.foldername.exists()
        self.uniques = []  # list of tuples of (filename, content)
        self.duplicates = {}
        self.content = []

    def iter_folder(self):
        """Main function to find duplicate and unique files in the filesystem."""
        for file in self.foldername.rglob("*.*"):
            with open(file, "r") as f:  # file is open for a brief period
                content = f.read()
            if content in self.content:
                for item in self.uniques:
                    if item[1] == content:  # same content
                        self.duplicates[item[0]].append(str(file))

            else:
                self.content.append(content)
                self.uniques.append((str(file), content))
                self.duplicates[str(file)] = []


if __name__ == "__main__":
    fol = FolderIterator()
    fol.iter_folder()
    print(fol.uniques)
    print(fol.duplicates)
