from src.LawnGrass import LawnGrass
from src.Product import Product
from src.PrintMixin import PrintMixin
from src.Smartphone import Smartphone


def test_print_mixin(capsys):
    Product("Iphone 15 Pro Max", "512GB, Gray space", 250000.0, 2)
    message = capsys.readouterr()
    assert message.out.strip() == 'Product(Iphone 15 Pro Max, 512GB, Gray space, 250000.0, 2)'

    Smartphone("HUAWEI", "Популярные смартфоны", 20000.0, 10, 90.0, 'nova',
               128, 'White')
    message = capsys.readouterr()
    assert message.out.strip() == 'Smartphone(HUAWEI, Популярные смартфоны, 20000.0, 10)'

    LawnGrass(
        "Газонная трава 3", "Выносливая трава", 600.0, 60, 'Russia', "10 дней",
        'Ярко-зеленый')
    message = capsys.readouterr()
    assert message.out.strip() == 'LawnGrass(Газонная трава 3, Выносливая трава, 600.0, 60)'
