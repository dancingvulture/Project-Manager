"""\
Interface to create, run, and view projects.\
"""


from src.command_line import parse_arguments
import src.aliases as aliases
import src.projects as projects


def main():
    args = parse_arguments()
    if args.mode == "new-project":
        projects.create(args.directory)
    elif args.mode == "aliases":
        aliases.propogate()
    else:
        raise ValueError(f"Invalid mode: {args.mode}")


if __name__ == "__main__":
    main()

