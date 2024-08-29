def test_Product_init(product):
    assert product.name == "Iphone 15"
    assert product.description == "512GB, Gray space"
    assert product.quantity == 8
    assert product.price == 210000.00


def test_Product_new_product(new_product):
    new_product1 = new_product
    assert new_product1.name == "Samsung Galaxy S23 Ultra"
    assert new_product1.description == '256GB, Серый цвет, 200MP камера'
    assert new_product1.price == 180000.0
    assert new_product1.quantity == 10

def test_Product_new_product_not_in_products(new_product_not_in_products):
    new_product1 = new_product_not_in_products
    assert new_product1.name == "Iphone 15 Pro Max"
    assert new_product1.description == '512GB, Gray space'
    assert new_product1.price == 250000.0
    assert new_product1.quantity == 2

def test_Product_price(capsys, product):
    product.price = -100
    message = capsys.readouterr()
    assert message.out.strip().split('\n')[-1] == 'Цена не должна быть нулевая или отрицательная'
    product.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == 'Цена не должна быть нулевая или отрицательная'
    product.price = 100
    assert product.price == 100

def test_product_add(product, product1):
    assert (product + product1) == 2130000.0

def test_product_str(product):
    assert str(product) == 'Iphone 15, 210000.0 руб. Остаток: 8 шт.'


