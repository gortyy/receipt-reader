from argparse import ArgumentParser

from receipt_reader import Parser, Reader
from receipt_reader.aggregator import Aggregator
from receipt_reader.translator import Translator


def main():
    args = parse_args()
    receipt_reader = Reader(args.file)
    contents = receipt_reader.read_image()

    receipt_parser = Parser(contents)
    from pprint import pp

    products = [Translator(product).translate() for product in receipt_parser.parse()]
    aggregator = Aggregator(products)
    pp(aggregator.aggregate())


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--file", type=str, required=True)
    parser.add_argument("--output-file", type=str, required=False)

    return parser.parse_args()


if __name__ == "__main__":
    main()
