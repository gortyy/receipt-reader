import pytest

from receipt_reader import Parser
from receipt_reader.product import Product


@pytest.fixture
def receipt_contents() -> str:
    return """\
        Śliwki 1,824 * 7,99 8,18
        Banany Premium 8.988 * 3,99 3,91
        Krewetki biał.mroż. _ 1 + 39,99 39,99
        MięsoMiel.WołowePor. 1 * 19,99 19,99
        Marchew luz 4.266 * 3.99 1,06
        Limetki 8,138 * 19,90 2,75
        Mleko św. 2%PET 2 + 3,49 6,98
        $er Grana Padano 1 * 14,49 14,49
        Cebula żółta 8.158 * 3,99 8,68
    """


def test_parse(receipt_contents):
    parser = Parser(receipt_contents)

    result = parser.parse()

    assert result == [
        Product(name="Śliwki", price=8.18),
        Product(name="Banany Premium", price=3.91),
        Product(name="Krewetki biał.mroż.", price=39.99),
        Product(name="MięsoMiel.WołowePor.", price=19.99),
        Product(name="Marchew luz", price=1.06),
        Product(name="Limetki", price=2.75),
        Product(name="Mleko św.", price=6.98),
        Product(name="$er Grana Padano", price=14.49),
        Product(name="Cebula żółta", price=8.68),
    ]
