from .exception import ReceiptParserException
from .product import Product


class Parser:
    def __init__(self, receipt_contents: str):
        self._receipt_contents = receipt_contents

    def parse(self) -> list[Product]:
        return [
            self._parse_line(line)
            for line in self._receipt_contents.splitlines()
            if self._contains_digit(line)
        ]

    @classmethod
    def _parse_line(cls, line: str) -> Product:
        ignored_chars = ("*", "+", "»", "«", "©", "_")
        for char in ignored_chars:
            line = line.replace(char, " ")

        digit_index = cls._find_first_digit_index(line)
        name = line[:digit_index].strip(" ,")
        price = cls._parse_price(line[digit_index:])

        return Product(name, price)

    @classmethod
    def _parse_price(cls, string: str) -> float:
        price = string[string.rfind(" ") :].strip().replace(",", ".")

        try:
            return float(price)
        except ValueError as ve:
            raise ReceiptParserException(
                f"Couldn't parse price in following string: {string}"
            ) from ve

    @classmethod
    def _find_first_digit_index(cls, line: str) -> int:
        for index, char in enumerate(line):
            if char.isdigit():
                return index

    @classmethod
    def _contains_digit(cls, line: str) -> bool:
        return any(digit in line for digit in "0123456789")
