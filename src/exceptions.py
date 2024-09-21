from typing import Any


class ZeroQuantityProduct(Exception):
    '''Создаем свое исключение'''
    def __init__(self, message: Any = None) -> None:
        super().__init__(message)
