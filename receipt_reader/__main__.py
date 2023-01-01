from pprint import pp

import typer

from receipt_reader import Parser, Reader
from receipt_reader.aggregator import Aggregator
from receipt_reader.db import DbClient
from receipt_reader.product import Product
from receipt_reader.translator import Translator

app = typer.Typer()


@app.command()
def insert_receipt(filepath: str):
    receipt_reader = Reader(filepath)
    contents = receipt_reader.read()

    receipt_parser = Parser(contents)

    products = [Translator(product).translate() for product in receipt_parser.parse()]
    aggregator = Aggregator(products)
    aggregator.aggregate()

    _insert(products)


@app.command()
def insert_manually(products: list[str]):
    parsed_products = []
    for product in products:
        name, price = product.split(":")
        product = Product(name, float(price))
        translator = Translator(product)
        parsed_products.append(translator.translate())

    _insert(parsed_products)


def _insert(products: list[Product]):
    client = DbClient("mongodb://admin:pass@localhost:27017/")
    insert_id = client.insert(products)
    pp(client.find(insert_id))


if __name__ == "__main__":
    app()
