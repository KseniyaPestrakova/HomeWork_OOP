class Category:
    '''Класс для представления продукта'''

    name: str
    description: str
    __products: list
    category_count = 0
    product_count: int

    def __init__(self, name: str, description: str, products: list):
        '''Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра.'''

        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count = len(products)

    @property
    def products(self):
        return self.__products

    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1



