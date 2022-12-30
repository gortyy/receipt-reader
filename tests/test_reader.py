from textwrap import dedent

import pytest


from receipt_reader import Reader


@pytest.fixture
def image_file_path() -> str:
    return "tests/resources/receipt.png"


def test_read_image(image_file_path):
    reader = Reader(image_file_path)

    result = reader.read_image()

    assert result == dedent(
        """\
            Jaja wol .wyb.M,L,XL 1 » 9,99 9,99
            Pepsi Regular 1 + 8,79 8,79
            BIO passata pomid. 1 + 7,49 7,49
            Pomidory malinowe 0,812 * 19,99 16,23
            Skyr pitny 2 * 4,47 8,94
            Skyr pitny 2 + 4,47 8,94
            Papryczki pikantne ©,044 « 38,00 1,67
            Mięso miel. z ind. 1 * 10,29 18,29
            Cebula szalotka 8,074 * 9,40 6,78
            Pieczywo Focaccia 2 + 6,99 13,08
            Cukinia 0,482 * 11,99 5,78
            Ketchup Heinz 1 » 6,99 6,99
            Ziem.jad.na fr.2kg 1 + 6,99 6,99
            Jabłko Pinova 8.868 * 3,99 3,43
            Skyr pitny 2 * 4,47 8,94
            Ser Moz. bez GMO 1 + 2,99 2,99
            Jogurt grecki 10% 1 + 2,66 2,66
            Sok bezp.tł.Solev, 3 * 6,99 28,97
            Kiwi szt. 6 * 0,89 5,34
            Ser Burrata 125g 1 + 6,99 6,99
            Mix sał.z ruk.166g 1» 4,99 4,99
            Tarez .KabanosyEasy 1 « 6,49 6,49
            Wędliny włoskie 1 « 12,99 12,99
            Śliwki 1,824 * 7,99 8,18
            Banany Premium 8.988 * 3,99 3,91
            Krewetki biał.mroż. _ 1 + 39,99 39,99

            MięsoMiel.WołowePor. 1 * 19,99 19,99

            Marchew luz 4.266 * 3.99 1,06
            Limetki 8,138 * 19,90 2,75
            Mleko św. 2%PET 2 + 3,49 6,98
            $er Grana Padano 1 * 14,49 14,49
            
            Cebula żółta 8.158 * 3,99 8,68
            
            PODODOŁRODDODODOOPDDOOOOWODODODOODCOŁO
        """
    )
