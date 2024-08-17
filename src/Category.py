from typing import Any

from src.Product import Product


class Category:
    """Класс для представления продукта"""

    name: str
    description: str
    __products: list
    category_count = 0
    product_count: int

    def __init__(self, name: str, description: str, products: list):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""

        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count = len(products)

    @property
    def products(self) -> Any:
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
        return products_str

    def add_product(self, product: Product) -> Any:
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products_list(self) -> Any:
        return self.__products
