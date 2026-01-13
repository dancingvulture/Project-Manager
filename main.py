"""
Interface to create, run, and view projects.
"""


import src.command as command


def main():
    handler = command.Handler()
    handler.run("welcome")
    while True:
        display_dir = handler.get_display_directory()
        cmd = input(f"~//{display_dir}> ")
        handler.run(cmd)


if __name__ == "__main__":
    main()
