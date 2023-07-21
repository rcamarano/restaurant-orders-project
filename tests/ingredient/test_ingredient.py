from src.models.ingredient import (
    Ingredient,
    Restriction,
) # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredients = ['frango', 'ovo', 'farinha']
    frango, ovo, farinha = [Ingredient(name) for name in ingredients]

    assert farinha != ovo
    assert farinha == farinha

    assert hash(ovo) != hash(farinha)
    assert hash(ovo) != hash(frango)
    assert hash(ovo) == hash(ovo)

    assert repr(ovo) == "Ingredient('ovo')"
    assert ovo.name == 'ovo'

    assert farinha.restrictions == {Restriction.GLUTEN}
