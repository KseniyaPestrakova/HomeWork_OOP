import pytest


def test_smartphone_init(smartphone1):
    assert smartphone1.name == "HUAWEI"
    assert smartphone1.description == "Популярные смартфоны"
    assert smartphone1.quantity == 10
    assert smartphone1.price == 20000.0
    assert smartphone1.model == 'nova'
    assert smartphone1.memory == 128
    assert smartphone1.color == 'White'
    assert smartphone1.efficiency == 90.0


def test_smartphone_add(smartphone1, smartphone2):
    assert smartphone1 + smartphone2 == 450000.0


def est_smartphone_add_error(smartphone1, lawngrass1):
    with pytest.raises(TypeError):
        result = smartphone1 + lawngrass1