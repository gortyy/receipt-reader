from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass
class Product:
    name: str
    price: float

    def as_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict) -> Product:
        return cls(d["name"], d["price"])
