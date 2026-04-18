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
        "directory",
        help="Name of the directory the project will be placed in."
    )


def _add_aliases_subparser(subparsers) -> None:
    parser = subparsers.add_parser(
        "aliases",
        help="Manage aliases.",
    )
    alias_subparsers = parser.add_subparsers(dest="func")
    
    _add_aliases_add_dir_subparser(alias_subparsers)
    _add_aliases_propogate_subparser(alias_subparsers)


def _add_aliases_add_dir_subparser(subparsers) -> None:
    parser = subparsers.add_parser(
        "add-dir",
        help="Add a new directory to the directories file, which the aliases"
             " file will propate to when the propogate function is ran."
    )
    parser.add_argument(
        "directory"
    )


def _add_aliases_propogate_subparser(subparsers) -> None:
    parser = subparsers.add_parser(
        "propogate",
        help="Propogate the master aliases.sh file to all projects, as well as"
             " any directory containd in the directories file."
    )

