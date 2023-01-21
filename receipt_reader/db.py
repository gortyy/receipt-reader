from datetime import datetime

from bson.objectid import ObjectId
from pymongo import MongoClient
from pymongo.collection import Collection

from receipt_reader.product import Product


class DbClient:
    def __init__(self, connection_string: str):
        self._client = MongoClient(connection_string)
        self._db = self._client.shopping_history
        self._receipts: Collection = self._db.receipts

    def insert(self, products: list[Product]) -> ObjectId:
        result = self._receipts.insert_one(
            {
                "products": [product.as_dict() for product in products],
                "created_at": datetime.today().replace(
                    hour=0, minute=0, second=0, microsecond=0
                ),
            }
        )
        return result.inserted_id

    def find(self, object_id: ObjectId) -> list[Product]:
        document = self._receipts.find_one({"_id": object_id})
        return [Product.from_dict(product) for product in document["products"]]

    def find_by_date(self, date: datetime) -> list[Product]:
        documents = self._receipts.find({"created_at": date})
        all_products = []

        for document in documents:
            all_products.extend(
                [Product.from_dict(product) for product in document.get("products")]
            )

        return all_products
