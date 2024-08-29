import pytest


def test_category(category1, category2):
    assert category1.name == "Смартфоны"
    assert category1.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert len(category1.products_list) == 2

    assert category2.name == "Телевизоры"
    assert category2.description == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    assert len(category2.products_list) == 2

    assert category2.category_count == 2
    assert category1.category_count == 2

def test_products_str(category2):
    assert category2.products == '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.45" QLED 2K, 105000.0 руб. Остаток: 4 шт.'

def test_add_product(product, category2):
    category2.add_product(product)
    assert category2.product_count == 3

def test_category_add(category2):
    assert str(category2) == 'Телевизоры, количество продуктов: 11 шт.'


def test_add_product_error(product, category2):
    with pytest.raises(TypeError):
        category2.add_product("Not a product")
