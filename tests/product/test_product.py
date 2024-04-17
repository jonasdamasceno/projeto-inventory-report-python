from inventory_report.product import Product


def test_create_product() -> None:
    product = {
        "id": "1",
        "product_name": "Leite",
        "company_name": "Parmalat",
        "manufacturing_date": "10/01/2024",
        "expiration_date": "10/02/2024",
        "serial_number": "1821318274",
        "storage_instructions": "Guardar em lugar ventilado e longe do sol",
    }

    product = Product(**product)

    for key, value in product.items():
        assert getattr(product, key) == value
