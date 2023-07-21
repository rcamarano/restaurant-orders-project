from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    lasanha = Dish("Lasanha", 30.0)
    assert lasanha.name == "Lasanha"
    assert lasanha.price == 30.0

    lasanha.add_ingredient_dependency(Ingredient("massa de lasanha"), 1)
    lasanha.add_ingredient_dependency(Ingredient("queijo mussarela"), 1)
    lasanha.add_ingredient_dependency(Ingredient("caldo de carne"), 1)

    assert lasanha.recipe == {
        Ingredient("massa de lasanha"): 1,
        Ingredient("queijo mussarela"): 1,
        Ingredient("caldo de carne"): 1,
    }

    assert lasanha.get_restrictions() == {
        Restriction.ANIMAL_DERIVED,
        Restriction.GLUTEN,
        Restriction.LACTOSE,
    }

    assert lasanha.get_ingredients() == {
        Ingredient("massa de lasanha"),
        Ingredient("queijo mussarela"),
        Ingredient("caldo de carne"),
    }

    frango_grelhado = Dish("Frango Grelhado", 25.0)

    assert frango_grelhado.name == "Frango Grelhado"
    assert frango_grelhado.price == 25.0

    frango_grelhado.add_ingredient_dependency(Ingredient("frango"), 1)
    frango_grelhado.add_ingredient_dependency(Ingredient("manteiga"), 1)
    frango_grelhado.add_ingredient_dependency(
        Ingredient("queijo provolone"), 1
    )

    assert frango_grelhado.recipe == {
        Ingredient("frango"): 1,
        Ingredient("manteiga"): 1,
        Ingredient("queijo provolone"): 1,
    }

    assert frango_grelhado.get_restrictions() == {
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
        Restriction.LACTOSE,
    }

    assert lasanha.__repr__() == "Dish('Lasanha', R$30.00)"
    assert frango_grelhado.__repr__() == "Dish('Frango Grelhado', R$25.00)"

    assert lasanha.__eq__(frango_grelhado) is False
    assert lasanha.__eq__(lasanha) is True

    assert lasanha.__hash__() == hash("Dish('Lasanha', R$30.00)")
    assert frango_grelhado.__hash__() == hash(
        "Dish('Frango Grelhado', R$25.00)"
    )

    with pytest.raises(TypeError) as error:
        Dish("Invalid Dish", "25")

    assert str(error.value) == "Dish price must be float."

    with pytest.raises(ValueError) as error:
        Dish("Invalid Dish", 0)

    assert str(error.value) == "Dish price must be greater then zero."
