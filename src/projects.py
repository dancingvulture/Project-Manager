"""
Module for creating new projects.
"""


import os
import subprocess
from src.files import Directories, FileTree


def create_new(project_name: str, directories: Directories) -> None:
    """
    Create a new project based off of the project template, and place it
    in the project directory in a folder named project_name.
    """
    project_directory = directories.projects + "\\" + project_name
    os.mkdir(project_directory)
    project_template = FileTree(directories.project_template)
    project_template.copy(project_directory)


def _create_venv(directory: str, folder=".venv") -> None:
    """
    Create a virtual venv in the stated directory.
    """
    python = "py" if os.name == "nt" else "python3"
    commands = [
        "powershell;"
        "cd", directory, ";",
        python, "-m", "venv", folder, ";",
        python, "-m", "pip", "install", "--upgrade", "pip", ";",
        python, "-m", "pip", "install", "ipython", ";",
        python, "-m", "pip", "install",  "rich",
    ]
    subprocess.run(commands, shell=True)

def _initialize_git(director: str) -> None:
    """
    Initialize a git repo in the target directory.
    """
