from argparse import ArgumentParser, Namespace


def main():
    parser = ArgumentParser(
        prog="wc.py",
        description="Word Count - counts words, lines, and bytes or characters in a file",
    )
    parser.add_argument(
        "filename",
        help="A path name of an input file. If no file operands are specified, the standard input is used.",
    )

    args: Namespace = parser.parse_args()
    print(f"{args.filename}")


if __name__ == "__main__":
    main()
