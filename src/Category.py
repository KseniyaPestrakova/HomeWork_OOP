from typing import Any

from src.exceptions import ZeroQuantityProduct
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

    def __str__(self) -> Any:
        quantity = 0
        for product in self.__products:
            quantity += product.quantity
        return f"{self.name}, количество продуктов: {quantity} шт."

    @property
    def products(self) -> Any:
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}"
        return products_str

    def add_product(self, product: Product) -> Any:
        if isinstance(product, Product):
            try:
                if product.quantity == 0:
                    raise ZeroQuantityProduct("Нельзя добавить продукт с нулевым количеством")
            except ZeroQuantityProduct as e:
                print(str(e))
            else:
                self.__products.append(product)
                Category.product_count += 1
                print("товар добавлен")
            finally:
                print("обработка добавления товара завершена")
        else:
            raise TypeError

    @property
    def products_list(self) -> Any:
        return self.__products

    def middle_price(self) -> Any:
        try:
            return round(sum([product.price for product in self.__products]) / len(self.__products), 2)
        except ZeroDivisionError:
            return 0
