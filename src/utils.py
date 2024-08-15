import json
import os
from typing import List

from src.Category import Category
from src.Product import Product


def read_json(path: str) -> List:
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))

    return categories


if __name__ == "__main__":
    json_categories = read_json("../data/products.json")
    print(json_categories[0].name)
    print(json_categories[0].description)
    print(len(json_categories[0].products))
