"""\
Retrieve and manage special directories.\
"""


import os
import json


_DIRECTORIES_FILE = "directories.json"


def get(name: str) -> str:
    """\
    Get the project directory from directories.json, if the file doesn't 
    exist, prompt the user to create it.\
    """
    if not os.path.exists(_DIRECTORIES_FILE):
        _create_directories_file()

    direcs = load()
    if not name in direcs:
        _create_directories_entry(direcs, name)
    
    return direcs[name]


def load() -> dict[str, str]:
    """\
    Loads the directories dictionary from the json.\
    """
    with open(_DIRECTORIES_FILE) as file:
        direcs = json.load(file)
    return direcs


def save(direcs: dict[str, str]) -> None:
    """\
    Saves the directories dict passed into this function to the directories file.\
    """
    with open(_DIRECTORIES_FILE, 'w') as file:
        json.dump(direcs, file)
    print(f"Saved {_DIRECTORIES_FILE}")
 

def _create_directories_file() -> None:
    """\
    Create an empty directories file.\
    """
    with open(_DIRECTORIES_FILE, 'w') as file:
        json.dump({}, file)


def _create_directories_entry(direcs: dict[str, str], name: str) -> None:
    """\
    Via user prompt, adds a new entry into the directories dictionary, and
    saves this new version into the directories file.\
    """
    print((f"{name} directory not found in {_DIRECTORIES_FILE}, please enter"
            " the value now."))
    path = input(f"{name}> ")
    direcs[name] = path
    save(direcs)

