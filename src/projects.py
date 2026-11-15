"""\
Module for creating new projects.\
"""


from datetime import datetime
import shutil
import os

import src._licenses as licenses
import src.aliases as aliases
import src.directories as directories


_TEMPLATES_DIR = "templates"
TEMPLATES = [
    "py-project",
    "c-project",
]

def create(directory: str,
           template: str,
           languages: list[str],
           no_gen=False,
           no_git=False
           ) -> None:
    """\
    Create a new project in the indicated directory.\
    """
    if os.path.exists(directory):
        raise ValueError(f"directory {directory} already exists.")

    _update_license()

    projects_dir = directories.get("projects")
    if template:
        shutil.copytree(
            f"{_TEMPLATES_DIR}/{template}",
            f"{projects_dir}/{directory}",
        )
    else:
        os.mkdir(f"{projects_dir}/{directory}")

    script_list = aliases.create_script_list(
        languages,
        no_gen,
        no_git
    )
    aliases.create_file(
        f"{projects_dir}/{directory}",
        script_list
    )
    print(f"Project {directory} successfully made in {projects_dir}")


def _update_license(directory: str=_TEMPLATES_DIR,
                    license_: str=licenses.MIT,
                    name: str="John Laney"
                    ) -> None:
    """\
    Create a license in the project template directory. Presently this mostly
    exists to make sure the year is up to date.\
    """
    year = datetime.now().year
    license_text = license_.format(year, name)

    for template in TEMPLATES:
        with open(f"{directory}/{template}/LICENSE", 'w') as file:
            file.write(license_text)
