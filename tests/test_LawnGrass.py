import pytest


def test_lawngrass_init(lawngrass1):
    assert lawngrass1.name == "Газонная трава 3"
    assert lawngrass1.description == "Выносливая трава"
    assert lawngrass1.quantity == 60
    assert lawngrass1.price == 600.0
    assert lawngrass1.country == 'Russia'
    assert lawngrass1.germination_period == '10 дней'
    assert lawngrass1.color == 'Ярко-зеленый'



def test_lawngrass_add(lawngrass1, lawngrass2):
    assert lawngrass1 + lawngrass2 == 63000.0


def est_lawngrass_add_error(smartphone1, lawngrass1):
    with pytest.raises(TypeError):
        result = smartphone1 + lawngrass1

