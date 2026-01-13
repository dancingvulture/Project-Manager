"""
Functions for doing file stuff or whatever.
"""


from dataclasses import dataclass
import os


_DIRECTORIES_FILE = "directories.txt"


@dataclass
class Directories:
    """
    Container for directories used in the program.
    """
    projects: str
    project_template: str
    master_bash_script: str
    relative_bash_script: str


@dataclass
class File:
    """
    Stores basic file information, just the filename (not including the
    directory) and its contents in plain text.
    """
    filename: str
    contents: str


class FileTree:
    """
    A class whose instance stores the structure, files (and their contents)
    of a file directory tree. The tree is implemented internally sa list,
    whose members are files (represented by the File class) and folders
    (represented by a list).

    I could definitely just use shutil for this project but I wanna make it.
    """
    def __init__(self, root_directory: str):
        self.root_directory = root_directory
        self._tree = self._get_file_tree(root_directory)

    def copy(self, directory: str) -> None:
        """
        Copies the file tree into the given directory, overwriting any files
        sharing the same names.
        """


    @staticmethod
    def _get_file_tree(root_directory: str) -> list[list, File]:
        """
        Given a root directory this function will recursively get all file and
        directory contents and add them to a list, whose members are files
        (represented by the File class) and folders (represented by a list).
        """

    @staticmethod
    def _get_file_contents(filename: str) -> str:
        """
        Grab all file contents as a string in plain text.
        """


    def __eq__(self, other: 'FileTree'):
        if isinstance(other, FileTree) and self._tree == other._tree:
            return True
        else:
            return False


def get_directories() -> Directories:
    """
    Retrieves the directory values from the file, creates an instance
    of the Directories class with those values, and returns it.
    """
    if not os.path.exists(_DIRECTORIES_FILE):
        _create_directories_file(_DIRECTORIES_FILE)

    directories_dict = _text_file_to_dict(_DIRECTORIES_FILE)
    return Directories(**directories_dict)


def create_file(path: str, contents: str, *, quiet=False) -> None:
    """
    Create a file on the given path with the given contents, the directories
    making up the path must already exist.
    """
    exists = os.path.exists(path)
    with open(path, 'w') as file:
        file.write(contents)

    if exists and not quiet:
        print(f"WARNING: {path} was overwritten")


def _create_directories_file(filename: str) -> None:
    """
    Create a directories file from user input.
    """
    print("directories file does not exist! Creating one..\n")

    directories_and_prompts = [
        ("projects", "Projects directory (full path) = "),
        ("tests", "Tests directory (full path) = ")
    ]
    directory_dict = {}
    print("Specify each directory")
    for directory, prompt in directories_and_prompts:
        directory_dict[directory] = input(prompt)

    _dict_to_text_file(directory_dict, filename)


def _text_file_to_dict(filename: str, separator="=") -> dict[str, str]:
    """
    Converts the contents of a text file to a dictionary. Syntax is as
    follows:
        - Each dict entry is a non-empty line.
        - Each entry must contain one and only one separator (default: =).
        - All text to the left of the separator is the key, while all text
          to the right is the value.
        - Keys and values are all strings.
        - Whitespace on the edges of keys and values is ignored (except \n).
    """
    text_dict = {}
    with open(filename) as file:
        for line in file.readlines():
            if line.isspace():  # skip if line is just whitespace.
                pass
            elif line.count(separator) != 1:
                raise Exception(f"Line must contain exactly one"
                                f" separator ({separator}): {line}")
            else:
                key, value = map(lambda x: x.strip(), line.split(separator))
                text_dict[key] = value
    return text_dict


def _dict_to_text_file(file_dict: dict[str, str], filename: str, separator="=") -> None:
    """
    Takes a file dict (the kind created by _text_file_to_dict), and turns it
    into a file using the same syntax.
    """
    contents = ""
    for key, value in file_dict.items():
        contents += key + " " + separator + " " + value + "\n"
    with open(filename, 'w') as file:
        file.write(contents)
