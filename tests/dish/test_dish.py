from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    parmegiana = Dish("Paregiana", 85.0)
    risoto = Dish("Risoto", 45.0)

    assert parmegiana.name == "Paregiana"
    assert parmegiana.price == 85.0

    assert risoto.name == "Risoto"
    assert risoto.price == 45.0

    assert hash(parmegiana) != hash(risoto)
    assert hash(parmegiana) == hash(Dish("Paregiana", 85.0))
    assert parmegiana == Dish("Paregiana", 85.0)

    assert hash(risoto) != hash(parmegiana)
    assert hash(risoto) == hash(Dish("Risoto", 45.0))
    assert risoto == Dish("Risoto", 45.0)

    assert str(parmegiana) == "Dish('Paregiana', R$85.00)"
    assert str(risoto) == "Dish('Risoto', R$45.00)"

    with pytest.raises(TypeError):
        Dish("Paregiana", "preço")  # type: ignore

    with pytest.raises(ValueError):
        Dish("Paregiana", -1.0)

    ingredient_parmegiana = Ingredient("carne")
    parmegiana.add_ingredient_dependency(ingredient_parmegiana, 1)

    assert ingredient_parmegiana in parmegiana.get_ingredients()
    assert Restriction.ANIMAL_DERIVED in parmegiana.get_restrictions()

    with pytest.raises(TypeError):
        Dish("Risoto", "preço")  # type: ignore

    with pytest.raises(ValueError):
        Dish("Risoto", -1.0)

    ingredient_risoto = Ingredient("queijo")
    risoto.add_ingredient_dependency(ingredient_risoto, 1)

    assert ingredient_risoto in risoto.get_ingredients()
    assert Restriction.ANIMAL_DERIVED in risoto.get_restrictions()
