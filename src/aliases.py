"""\
Manage bash scripts.\
"""


import os
import shutil

import src.directories as directories


ALIASES_FILE = "aliases.sh"


def propogate() -> None:
    """\
    Propogate the master aliases file to all projects in the projects folder.
    As well as any other folders in the directories file.\
    """
    project_directory = directories.get("projects")
    other_dirs = directories.load()
    other_dirs.pop("projects")

    targets = []
    for project_folder in os.scandir(project_directory):
        try: 
            alias_path = shutil.copy(ALIASES_FILE, project_folder.path)
            targets.append(alias_path)
        except shutil.SameFileError:
            pass

    for path in other_dirs.values():
        alias_path = shutil.copy(ALIASES_FILE, path)
        targets.append(alias_path)

    print("Successfully updated:")
    for path in targets:
        print(path)
  
