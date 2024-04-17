from typing import List

from inventory_report.product import Product


class Inventory:
    def __init__(self, data: List[Product] | None = None) -> None:
        self._data: List[Product] = data if data else []

    @property
    def data(self) -> List[Product]:
        return self._data

    def add_data(self, data: List[Product]) -> None:
        self._data.extend(data)
