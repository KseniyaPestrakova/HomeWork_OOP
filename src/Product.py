from typing import Any


class Product:
    """Класс для представления продукта"""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, new_product: dict, products_list: list) -> Any:
        '''Классметод для добавления нового продукта с проверкой на уже существующие продукты в списке продуктов'''
        for product in products_list:
            if new_product["name"] == product.name:
                product.quantity += new_product["quantity"]
                if new_product["price"] >= product.price:
                    product.price = new_product["price"]
                return Product(product.name, product.description, product.price, product.quantity)
            else:
                return cls(
                    new_product["name"], new_product["description"], new_product["price"], new_product["quantity"]
                )

    @property
    def price(self) -> Any:
        '''Геттер для вывода цены'''
        return self.__price

    @price.setter
    def price(self, new_price: float) -> Any:
        '''Сеттер для установления новой цены с проверкой на нулевые и отрицательные значения'''
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price
