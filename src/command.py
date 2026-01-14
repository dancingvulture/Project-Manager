"""
Public module for handling commands, contains the Handler class.
"""


import re
import subprocess
import os
import src._cmd as cmd


class Handler:
    """
    Class for taking in and executing all user commands.
    """
    def __init__(self):
        self.aliases = {}
        self._commands: list[cmd.Command] = []  # Should initialize all command classes.
        self._prj_dir, self._test_dir = self._get_directories()
        self._new_prj_template_dir = "new project template"
        separators = [";", "&&"]
        self._split_pattern = self._create_command_split_pattern(*separators)

    def run(self, command: str) -> None:
        """
        Given a user command input, parse the command and hand it to the
        correct routine so the command can be run.
        """
        command = self._convert_aliases(command)

        if self._is_system_command(command):
            prefix = self._get_prefix()
            command = prefix + command.split(" ")
            subprocess.run(command, shell=True)

        else:
            self._execute_command(command)

    def get_display_directory(self) -> str:
        """
        Get the directory that will be displayed in the input prompt.
        """
        working_dir = os.getcwd()
        return working_dir.replace(self._prj_dir, "")

    def _get_directories(self) -> tuple[str, str]:
        """
        Get the project and test directories.
        """

    def _convert_aliases(self, command: str) -> str:
        """
        Work through every term in the command, substituting any known
        aliases for their full versions.
        """
        # Split the command by any separators, and then replace all aliases
        # line by line.
        lines = re.split(self._split_pattern, command)
        lines_new = []
        for line in lines:
            for command_ in self._commands:
                line = command_.replace_alias(line)
            lines_new.append(line)

        # Then put it back together, making sure the locations of the
        # original separators are preserved.
        separators = re.compile(self._split_pattern).findall(command)
        command_new = lines_new.pop(0)
        for sep in separators:
            command_new += sep + lines_new.pop(0)



    def _is_system_command(self, command: str) -> bool:
        """
        A system command is any command that (after aliases are swapped out)
        """


    def _get_prefix(self) -> list[str]:
        """
        Get the prefix that needs to be put in front of all subprocess
        commands to get them to work properly.
        """

        command = ["powershell", "-NoProfile;"] if os.name == "nt" else []
        command += ["cd", f"{self.working_directory};"]
        command += self._activate_venv
        return command

    def _execute_command(self, cmd) -> None:
        pass

    def _construct_subprocess_command(self,
                                      cmd: str,
                                      *,
                                      venv_prefix=False,
                                      ) -> list[str]:
        """
        Takes the cmd string (and assumes any aliases are substituted out)
        and constructs a subprocess command, adding any platform dependant
        prefixes, and optionally the venv_prefix (default False).
        """

    @staticmethod
    def _create_command_split_pattern(*separators:str) -> str:
        """
        Regex splitting function
        """
        pattern = ""
        for sep in separators:
            pattern += f"{sep}\\s*|"
        return pattern[:-1]  # Cut off last |
