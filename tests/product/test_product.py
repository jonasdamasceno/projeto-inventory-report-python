from inventory_report.product import Product


def test_create_product() -> None:
    product = Product(
        "1",
        "aptamil",
        "Danone",
        "29/11/2023",
        "30/05/2025",
        "1821318274",
        "Fórmula infantil de seguimento para lactentes",
    )

    assert product.id == "1"
    assert product.product_name == "aptamil"
    assert product.company_name == "Danone"
    assert product.manufacturing_date == "29/11/2023"
    assert product.expiration_date == "10/02/2024"
    assert product.serial_number == "1821318274"
    assert (
        product.storage_instructions
        == "Fórmula infantil de seguimento para lactentes"
    )
