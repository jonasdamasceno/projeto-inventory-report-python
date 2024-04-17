from inventory_report.product import Product


def test_product_report(capsys) -> None:
    id = "1"
    product_name = "Hydra bébé"
    company_name = "Mustela"
    manufacturing_date = "11/11/2022"
    expiration_date = "11/11/2025"
    serial_number = "123456789"
    storage_instructions = "frágil"
    product = Product(
        id,
        product_name,
        company_name,
        manufacturing_date,
        expiration_date,
        serial_number,
        storage_instructions,
    )

    response = str(product)

    expected_response = (
        f"The product {id} - {product_name} "
        f"with serial number {serial_number} "
        f"manufactured on {manufacturing_date} "
        f"by the company {company_name} "
        f"valid until {expiration_date} "
        "must be stored according to the following instructions: "
        f"{storage_instructions}."
    )

    assert response == expected_response
