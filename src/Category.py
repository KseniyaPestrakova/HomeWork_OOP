class Category:
    name: str
    description: str
    products: list
    category_count: int
    product_count: int

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.category_count = 1
        Category.product_count = len(products)