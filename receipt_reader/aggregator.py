from receipt_reader.product import Product


class Aggregator:
    def __init__(self, products: list[Product]):
        self._products = products

    def aggregate(self) -> list[Product]:
        products = {}

        for product in self._products:
            aggregated_product = products.get(product.name)
            if aggregated_product:
                products[product.name] += product.price
            else:
                products[product.name] = product.price

        return [Product(name, price) for name, price in products.items()]
