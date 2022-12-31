from receipt_reader.product import Product


class Translator:
    def __init__(self, product: Product):
        self._product = product
        self._translations = {
            "Jaja wol .wyb.M,L,XL": "jajka",
            "BIO passata pomid.": "passata",
            "Mięso miel. z ind.": "mięso mielone z indyka",
            "Ziem.jad.na fr.": "ziemniaki",
            "Jabłko Pinova": "jabłka",
            "Ser Moz. bez GMO": "ser",
            "Sok bezp.tł.Solev": "sok",
            "Mix sał.z ruk.": "mix sałat",
            "Tarez .KabanosyEasy": "kabanosy",
            "Krewetki biał.mroż.": "krewetki",
            "MięsoMiel.WołowePor.": "mięso mielone wołowe",
        }
        self._ignored_words = {
            "luz",
            "św.",
            "premium",
            "szt.",
            "heinz",
            "regular",
            "heinz",
        }
        self._replace_chars = {
            ("$", "s"),
        }

    def translate(self) -> Product:
        name = self._translations.get(self._product.name, self._product.name.lower())

        for ignored_word in self._ignored_words:
            name = name.replace(ignored_word, "")

        for old, new in self._replace_chars:
            name = name.replace(old, new)

        return Product(name.strip(), self._product.price)
