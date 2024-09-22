from typing import Any

from src.BaseProduct import BaseProduct
from src.PrintMixin import PrintMixin


class Product(BaseProduct, PrintMixin):
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
        if quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__(name, description, price, quantity)

    def __str__(self) -> Any:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> Any:
        if isinstance(other, Product):
            return self.__price * self.quantity + other.__price * other.quantity
        raise TypeError

    @classmethod
    def new_product(cls, new_product: dict, products_list: list) -> Any:
        """Классметод для добавления нового продукта с проверкой на уже существующие продукты в списке продуктов"""
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
        """Геттер для вывода цены"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> Any:
        """Сеттер для установления новой цены с проверкой на нулевые и отрицательные значения"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price
