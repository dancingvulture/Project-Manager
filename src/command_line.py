"""\
Handle command line arguments.\
"""


import argparse


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
         prog="Project Manager",
         description="Create new projects based off of the new project"
                     " template, or propagate the aliases bash script to"
                     " all projects in the projects directory."
    )
    subparsers = parser.add_subparser(
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
        "directory",
        help="Name of the directory the project will be placed in."
    )


def _add_aliases_subparser(subparsers) -> None:
    parser = subparsers.add_parser(
        "aliases",
        help="Propogate aliases.sh to all projects.",
    )
    

