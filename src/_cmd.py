"""
Contains all command classes and base classes.
"""


import re
import os
import subprocess


class Command:
    """
    Base class for commands. Some commands are simple, some are complex and
    might need arbitrary code. This is only meant to serve as a parent class
    for specific commands. Init arguments are the following:
        - command_text: A string giving the exact text of the command.
        - alias: A string giving the command's alias.
        - category: A string giving the command's category.
        - help_text: A string giving the help text displayed by the help command.
        - venv: A boolean indicating if the command should be run inside a virtualenv.
        - args: An optional string giving the type of arguments passed to the command.
          This is purely for display purposes when showing the command in the help
          function.
    """
    def __init__(self,
                 command_text: str,
                 alias: str,
                 category: str,
                 help_text: str,
                 *,
                 venv: bool = False,
                 pos_args: list[str] | None = None,
                 opt_args: list[str] | None = None,
                 ):
        self.command_text = self._py_replacer(command_text)
        self.displayed_command_text = self.command_text + args
        self.alias = alias
        self.displayed_alias_text = alias + args
        self.category = category
        self.help_text = help_text
        self._alias_pattern = self._create_alias_pattern(alias)

        if os.name == "nt":  # this should be moved to a command.
            self._venv_cmd = ".\\.venv\\Scripts\\Activate.ps1;"
        else:
            self._venv_cmd = "source .venv/bin/activate;"
        self._subprocess_cmd = self._create_subprocess_cmd(command_text, venv=venv)

    def run(self, *args) -> None:
        """
        Execute the command. Providing any args if needed.
        """
        raise Exception(f"This method of {self.__class__} must be overwritten by a descendant")

    def replace_alias(self, command: str) -> str:
        """
        Given a command, replace anything matching the alias pattern with
        the command substitution text. This assumes the command is a single
        line (i.e. not something like git init; git log). Also, that each alias
        is present only at the beginning of a line.
        """
        return re.sub(self._alias_pattern, self.command_text, command)

    def _create_subprocess_cmd(self,
                               command_text: str,
                               *,
                               venv=False
                               ) -> str:
        """
        Creates the command that will be passed into subprocess.run().
        """
        prefix = self._create_cmd_prefix(venv=venv)
        return prefix + command_text

    def _create_cmd_prefix(self, *, venv=False) -> str:
        """
        Add any necessary prefix commands for a subprocess command.
        """
        prefix = "powershell -NoProfile;" if os.name == "nt" else ""
        prefix += self._venv_cmd if venv else ""
        return prefix

    @staticmethod
    def _create_alias_pattern(alias: str) -> str:
        """
        A regular expression pattern used for replacing the alias with the
        full command text.
        """
        return f"^{alias}"

    @staticmethod
    def _py_replacer(command_text: str) -> str:
        """
        On unix the shortcut for python's interpreter is python3, while on
        Windows it tends to be py. This method checks the platform at makes
        sure the correct shortcut is used.
        """
        if os.name != "nt":
            return re.sub("^py", "python3", command_text)
        else:
            return command_text


class SystemCommand(Command):
    """
    A descendant of Command, deals with a specific subset of commands called
    system commands. Which are just commands that are minimally processed and
    then put directly into the subprocess.run() function.
    """
    def run(self, *args) -> None:
        """
        Run the command text through subprocess.run()
        """
        subprocess.run(self._subprocess_cmd, shell=True)


class GitInit(SystemCommand):
    """
    Initialize a git repo.
    """
    def __init__(self):
        super().__init__(
            command_text="git init",
            alias="gi",
            category="git",
            help_text="Initialize a git repository",
        )


