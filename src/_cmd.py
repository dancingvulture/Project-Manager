"""
Contains all command classes and base classes.
"""


import re


class Command:
    """
    Base class for commands. Some commands are simple, some are complex and
    might need arbitrary code. This is only meant to serve as a parent class
    for specific commands.
    """
    def __init__(self, command_text: str, alias: str, category: str):
        self.command_text = command_text
        self.alias = alias
        self.category = category
        self._regex_func = self._create_regex_func(command_text)

    def run(self, *args) -> None:
        """
        Execute the command. Providing any args if needed.
        """
        raise Exception(f"This method of {self.__class__} must be overwritten by a descendant")

    def help(self) -> str:
        """
        Contains any help text needed to explain the command.
        """
        raise Exception(f"This method of {self.__class__} must be overwritten by a descendant")

    def is_in(self, cmd: str) -> bool:
        """
        Check whether this command is present inside the command string.
        """
        if self._regex_func(cmd):
            return True
        else:
            return False

    def _create_regex_func(self, command_test: str) -> re.Pattern.search:
        """
        Creates a regex function to find the command inside command strings.
        """

    def _create_regex_pattern(self, command_text: str) -> str:
        """
        Given a command text, produce a regex pattern that will be able to
        locate the command within
        """
