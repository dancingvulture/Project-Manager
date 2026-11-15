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

GENERAL_ALIASES_FILE = 'general-aliases.sh'
GIT_ALIASES_FILE = 'git-aliases.sh'
LANG_SPECIFIC_ALIAS_FILES = {
    'python': 'python-aliases.sh',
    'c': 'c-aliases.sh'
}
SCRIPT_COMMENT_PREFIX = "SCRIPT_FILES:"
REGEX_FUNCS = {
    'alias': re.compile(".*alias (.*)=(?P<quote>['\"])(.*)(?P=quote)").findall,
    'table-name': re.compile("(.*)-aliases\\.sh").findall,
    'comment': re.compile(f"# {SCRIPT_COMMENT_PREFIX}.*").findall,
    'scripts-used': re.compile(f"\\w+\\.sh").findall
}
ALIAS_TABLE_WIDTH = 80


def _create_aliases_file_contents(script_files: list[str]) -> str:
    """\
    Given a language, build a string that will be the contents of the aliases file.\
    """
    script_files_comment = f"{SCRIPT_COMMENT_PREFIX}" + ', '.join(script_files)
    alias_text= ""      # Bash alias declarations that make usable aliases.
    alias_tables = ""   # The help-text tables describing the aliases.
    for filename in script_files:
        contents = _get_alias_file_content(filename) + "\n"
        alias_text += contents + "\n"
        alias_tables += _get_alias_table(filename, contents)
    bash_alias_help_func = _create_bash_alias_help_func(alias_tables)
    return script_files_comment + '\n' + bash_alias_help_func + '\n' + alias_text


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
    name: str = re_func(filename)[0]
    return name.capitalize()


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
    table_str = re.sub('\n', '\\\\n', alias_tables)
    table_str = re.sub('\x1b\\[\\dm', '', table_str)  # Remove ANSI escape sequences.
    table_str = re.sub('"', '\\"', table_str)
    return f"function aliases() {{\n printf \"{table_str}\" \n}}\n"


def create_script_list(languages: list[str],
                       no_gen: bool,
                       no_git: bool
                       ) -> list[str]:
    """\
    Take cmd line argument values and turn them into a single list of scripts.\
    """
    script_files = [LANG_SPECIFIC_ALIAS_FILES[lang] for lang in languages]
    # Prepend general and git aliases.
    if not no_git: script_files = [GIT_ALIASES_FILE] + script_files
    if not no_gen: script_files = [GENERAL_ALIASES_FILE] + script_files
    return script_files


def create_file(directory: str, script_files: list[str]) -> None:
    """\
    Creates an aliases.sh file in the indicated directory.\
    """
    content = _create_aliases_file_contents(script_files)
    with open(f"{directory}/{ALIASES_FILE}", "w") as file:
        file.write(content)


def _get_script_list(alias_filepath: str) -> list[str]:
    """\
    Reads the comment that script file generations create to grab
    what files it's comprised of.\
    """
    with open(alias_filepath) as file:
        content = file.read()
        comment = REGEX_FUNCS['comment'](content)[0]
        script_list = REGEX_FUNCS['scripts-used'](comment)
    return script_list


def _update_aliases(filepath: str) -> None:
    """
    Given the filepath of an alias file, update it with the latest versions.
    """
    script_list = _get_script_list(filepath)
    create_file(filepath, script_list)


def propagate() -> None:
    """\
    Propagate the master aliases file to all projects in the projects folder.
    As well as any other folders in the directories file.\
    """
    project_directory = directories.get("projects")
    other_dirs = directories.load()
    other_dirs.pop("projects")

    updated = []
    for project_folder in os.scandir(project_directory):
        alias_path = f"{project_folder.path}/{ALIASES_FILE}"
        _update_aliases(alias_path)
        updated.append(alias_path)

    for path in other_dirs.values():
        alias_path = f"{path}/{ALIASES_FILE}"
        _update_aliases(alias_path)
        updated.append(alias_path)

    print("Successfully updated:")
    for path in updated:
        print(path)
