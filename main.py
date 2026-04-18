"""\
Interface to create, run, and view projects.\
"""


from src.command_line import parse_arguments
import src.aliases as aliases
import src.projects as projects
import src.directories as directories


def main():
    args = parse_arguments()
    if args.mode == "new-project":
        projects.create(args.directory)

    elif args.mode == "aliases":
        if args.func == "propogate":
            aliases.propogate()
        else:
            directories.get(args.directory)
    else:
        raise ValueError(f"Invalid mode: {args.mode}")


if __name__ == "__main__":
    main()

