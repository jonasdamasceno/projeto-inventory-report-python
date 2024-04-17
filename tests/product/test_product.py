from inventory_report.product import Product


def test_create_product() -> None:
    product_data = Product(
        "1",
        "Hydra bébé",
        "Mustela",
        "11/11/2022",
        "11/11/2025",
        "123456789",
        "frágil",
    )

    assert product_data.product_name == "Hydra bébé"
    assert product_data.company_name == "Mustela"
    assert product_data.manufacturing_date == "11/11/2022"
    assert product_data.expiration_date == "11/11/2025"
    assert product_data.serial_number == "123456789"
    assert product_data.id == "1"
    assert (
        product_data.storage_instructions
        == "frágil"
    )
