from abc import ABC, abstractmethod
from typing import Dict, Type

from inventory_report.product import Product
import json
import csv


class Importer(ABC):
    def __init__(self, path: str) -> None:
        self.path = path

    @abstractmethod
    def import_data(self) -> list[Product]:
        pass


class JsonImporter(Importer):
    def import_data(self) -> list[Product]:
        with open(self.path, "r") as file:
            json_data = json.load(file)
            products = []
            for item in json_data:
                product = Product(
                    item["id"],
                    item["product_name"],
                    item["company_name"],
                    item["manufacturing_date"],
                    item["expiration_date"],
                    item["serial_number"],
                    item["storage_instructions"],
                )
                products.append(product)
            return products


class CsvImporter:
    def import_data(self) -> list[Product]:
        with open(self.path, "r", encoding="utf-8") as file:
            csv_data = csv.DictReader(file)
            products = []
            for item in csv_data:
                product = Product(
                    item["id"],
                    item["product_name"],
                    item["company_name"],
                    item["manufacturing_date"],
                    item["expiration_date"],
                    item["serial_number"],
                    item["storage_instructions"],
                )
                products.append(product)
            return products

# Não altere a variável abaixo


IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
