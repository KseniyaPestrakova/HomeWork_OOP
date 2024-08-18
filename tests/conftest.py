import pytest

from src.Category import Category
from src.Product import Product


@pytest.fixture
def category1():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        products=[
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        ]
    )


@pytest.fixture
def category2():
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        products=[
            Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7),
            Product("45\" QLED 2K", "Ambient подсветка", 105000.0, 4)
        ]
    )


@pytest.fixture
def product():
    return Product(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8
    )

@pytest.fixture
def product1():
    return Product(
        name="Iphone 14 Pro Max",
        description="512GB, Black",
        price=150000.0,
        quantity=3
    )


@pytest.fixture
def new_product():
    return Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5},
        [
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        ]
        )

@pytest.fixture
def new_product_not_in_products():
    return Product.new_product(
        {"name": "Iphone 15 Pro Max", "description": "512GB, Gray space", "price": 250000.0,
         "quantity": 2},
        [
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        ]
        )
