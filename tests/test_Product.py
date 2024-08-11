def test_Product_init(product):
    assert product.name == "Iphone 15"
    assert product.description == "512GB, Gray space"
    assert product.quantity == 8
    assert product.price == 210000.00
