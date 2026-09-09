import argparse
import sys
from importlib.metadata import metadata


def get_metadata():
    data = metadata("teo")

    NAME = data["name"]
    VERSION = data["version"]
    SUMMARY = data["summary"]

    return {"prog": NAME, "version": VERSION, "description": SUMMARY}


def main():
    arg_parser = argparse.ArgumentParser(
        prog=get_metadata()["prog"],
        description=get_metadata()["description"],
        epilog="Made by Teo209 aka Piton\n",
        add_help=False,
    )

    arg_parser.add_argument("-h", "--help",
                            help="show this help message and exit",
                            action="help"
                            )
    arg_parser.add_argument("-v", "--version", 
                            help="show version",
                            action="version", version=f"{arg_parser.prog} {get_metadata()["version"]}"
                            )
    arg_parser.add_argument("file", 
                            nargs="?", 
                            help=".teo source file to execute"
                            )
    
    args = arg_parser.parse_args();
    
    if args.file is None:
        arg_parser.print_help()
        return 0


    try:
        with open(args.file, "r") as file:
            source = file.read()
    except FileNotFoundError:
        print(f"Error: File '{args.file}' not found. Please provide a valid file path.")
        return 1
    except Exception as e:
        print(f"Error reading file '{args.file}': {e}.")
        return 1

    print(source)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
