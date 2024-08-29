class PrintMixin:
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.quantity = quantity
        self.price = price
        self.description = description
        self.name = name
        print(repr(self))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
