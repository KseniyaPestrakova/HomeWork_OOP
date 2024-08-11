from src.utils import read_json


def test_read_json():
    json_categories = read_json("../data/products.json")
    assert json_categories[0].name == "Смартфоны"
    assert json_categories[0].description == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    assert len(json_categories[0].products) == 3