"""
Public module for handling commands, contains the Handler class.
"""


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

        if os.name == "nt":  # this should be moved to a command.
            self._activate_venv = [".\\.venv\\Scripts\\Activate.ps1;"]
        else:
            self._activate_venv = ["source" ".venv\\Scripts\\activate;"]

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
        for alias, full_term in self.aliases.items():
            command = command.replace(alias, full_term)
        return command

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

