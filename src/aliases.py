"""\
Manage bash scripts.\
"""


import os
import shutil
import re

from rich.table import Table
from rich.console import Console
from rich.box import ASCII2

import src.directories as directories


ALIASES_FILE = "aliases.sh"
BASH_SCRIPTS_DIR = "bash-scripts"
SCRIPT_FILES = {
    'python': ('general-aliases.sh', 'python-aliases.sh', 'git-aliases.sh'),
    'c': ('general-aliases.sh', 'c-aliases.sh', 'git-aliases.sh')
}
REGEX_FUNCS = {
    'alias': re.compile(".*alias (.*)=(?P<quote>['\"])(.*)(?P=quote)").findall,
    'table-name': re.compile("(.*)-aliases\\.sh").findall
}
ALIAS_TABLE_WIDTH = 80


def _create_aliases_file_contents(language: str) -> str:
    """\
    Given a language, build a string that will be the contents of the aliases file.\
    """
    alias_text= ""      # Bash alias declarations that make usable aliases.
    alias_tables = ""   # The help-text tables describing the aliases.
    for filename in SCRIPT_FILES[language]:
        contents = _get_alias_file_content(filename) + "\n"
        alias_text += contents + "\n"
        alias_tables += _get_alias_table(filename, contents)

    bash_alias_help_func = _create_bash_alias_help_func(alias_tables)


def _get_alias_file_content(filename: str) -> str:
    """\
    Given an alias filename, return all the contents as a string.
    """
    with open(f"{BASH_SCRIPTS_DIR}/{filename}") as file:
        contents = file.read()
    return contents


def _get_alias_table(filename: str, contents: str) -> str:
    """\
    Scanning through the contents of an alias file, create a formatted table
    that shows each alias and its definition.\
    """
    name = _get_table_name(filename)
    alias_definitions = _get_alias_definitions(contents)
    table = _create_table(name, alias_definitions)
    console = Console()
    with console.capture() as capture:
        console.print(table)
    return capture.get()


def _get_table_name(filename: str) -> str:
    """\
    Get the table name from the filename, assumes a very specific format.\
    """
    re_func = REGEX_FUNCS['table-name']
    name = re_func(filename)[0]
    return name


def _get_alias_definitions(contents: str) -> list[tuple[str, str]]:
    """\
    Exploit the regularity of bash syntax to grab the alias names and 
    definitions, putting them into a list of 2-tuples (name, definition).\
    """
    re_func = REGEX_FUNCS['alias']
    results = re_func(contents)
    return [(alias, defin) for alias, _, defin in results]


def _create_table(name: str, alias_defs: list[tuple[str, str]]) -> Table:
    """\
    Given the table's name and some alias definitions, create a rich table.\
    """
    table = Table(
        title=name,
        width=ALIAS_TABLE_WIDTH,
        box=ASCII2,
        title_justify="center",
    )
    table.add_column("alias")
    table.add_column("definition")

    for alias, defi in alias_defs:
        table.add_row(alias, defi)

    return table


def _create_bash_alias_help_func(alias_tables: str) -> str:
    """\
    Now that we have the raw text of the table, we need to put it inside a
    bash function, which will be what actually ends up in the alias file.\
    """
    


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
  
