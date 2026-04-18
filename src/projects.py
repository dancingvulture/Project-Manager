"""\
Module for creating new projects.\
"""


from datetime import datetime
import shutil
import os

import src._licenses as licenses
import src.aliases as aliases
import src.directories as directories


_NEW_PROJECT_TEMPLATE_DIR = "new project template"


def create(directory: str) -> None:
    """\
    Create a new project in the indicated directory.\
    """
    if os.path.exists(directory):
        raise ValueError(f"directory {directory} already exsits.")

    _update_license()
    _update_aliases()

    projects_dir = directories.get("projects")
    shutil.copytree(
        _NEW_PROJECT_TEMPLATE_DIR,
        f"{projects_dir}/{directory}",
    )
    print(f"Project {directory} successfully made in {projects_dir}")


def _update_license(directory: str=_NEW_PROJECT_TEMPLATE_DIR,
                    license_: str=licenses.MIT,
                    name: str="John Laney"
                    ) -> None:

    """\
    Create a license in the project template directory. Presently this mostly
    exists to make sure the year is up to date.\
    """
    year = datetime.now().year
    license_text = license_.format(year, name)

    with open(f"{directory}/LICENSE", 'w') as file:
        file.write(license_text)


def _update_aliases(directory: str=_NEW_PROJECT_TEMPLATE_DIR,
                    alias_filename: str=aliases.ALIASES_FILE,
                    ) -> None:
    """\
    Copy the master aliases file into the new project template.\
    """
    with open(alias_filename) as file:
        contents = file.read()

    with open(f"{directory}/{alias_filename}", 'w') as file:
        file.write(contents)

