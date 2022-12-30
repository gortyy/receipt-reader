from argparse import ArgumentParser

from .reader import Reader
from .parser import Parser


def main():
    args = parse_args()
    receipt_reader = Reader(args.file)
    contents = receipt_reader.read_image()

    receipt_parser = Parser(contents)
    from pprint import pp

    pp(receipt_parser.parse())


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--file", type=str, required=True)
    parser.add_argument("--output-file", type=str, required=False)

    return parser.parse_args()


if __name__ == "__main__":
    main()
