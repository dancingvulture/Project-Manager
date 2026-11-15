"""\
Handle command line arguments.\
"""


import argparse
from src.projects import TEMPLATES


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
         prog="Project Manager",
         description="Create new projects based off of the new project"
                     " template, or propagate the aliases bash script to"
                     " all projects in the projects directory."
    )
    subparsers = parser.add_subparsers(
        dest="mode",
    )
    
    _add_project_subparser(subparsers)
    _add_aliases_subparser(subparsers)

    return parser.parse_args()


def _add_project_subparser(subparsers) -> None:
    parser = subparsers.add_parser(
        "new-project",
        help="Create a new project",
    )
    parser.add_argument(
        "--template", "-te",
        help="Select the template to use,",
        choices=TEMPLATES,
        default='',
    )
    parser.add_argument(
        "--no-general", "-nge",
        help="Don't include the general-aliases in aliases.sh",
        action="store_true"
    )
    parser.add_argument(
        "--no-git", "-ngi",
        help="Don't include the git-aliases in aliases.sh",
        action="store_true"
    )
    parser.add_argument(
        "--languages", "-la",
        help="List languages (separated by commas), whose associated alias"
             " files you want to include. Options ",
        type=lambda x: [y.strip().casefold() for y in x.split(',')],
        default=[]
    )
    parser.add_argument(
        "directory",
        help="Name of the directory the project will be placed in. This is not"
             " the path just the label it will have in the json, the program"
             " will prompt you for the path."
    )


def _add_aliases_subparser(subparsers) -> None:
    parser = subparsers.add_parser(
        "aliases",
        help="Manage aliases.",
    )
    alias_subparsers = parser.add_subparsers(dest="func")
    
    _add_aliases_add_dir_subparser(alias_subparsers)
    _add_aliases_propagate_subparser(alias_subparsers)


def _add_aliases_add_dir_subparser(subparsers) -> None:
    parser = subparsers.add_parser(
        "add-dir",
        help="Add a new directory to the directories file, which the aliases"
             " file will propagate to when the propagate function is ran."
    )
    parser.add_argument(
        "directory"
    )


def _add_aliases_propagate_subparser(subparsers) -> None:
    parser = subparsers.add_parser(
        "propagate",
        help="Propagate the master aliases.sh file to all projects, as well as"
             " any directory contained in the directories file."
    )
