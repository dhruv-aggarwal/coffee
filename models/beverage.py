from .beverage_type import BeverageType
from .quantity_unit import QuantityUnit
from .ingredient import Ingredient
from .ingredient_holder import IngredientHolder
from exceptions.invalid_ingredient_exception import InvalidIngredientException

'''
Class defines the model for each beverage

Preparation time, method can be added as extention.
'''
class Beverage():
    def __init__(self, *args, **kwargs):
        self.beverage_type = kwargs.get("beverage_type")
        self.preparation_details = self.parse(kwargs.get("preparation_details"))

    def parse(self, beverage_detail_map):
        preparation_details = {}
        for ingr in beverage_detail_map:
            if ingr not in Ingredient.get_values():
                raise InvalidIngredientException(ingr, Ingredient.get_values())
            else:
                preparation_details[ingr] = IngredientHolder(
                    ingredient_type=ingr,
                    quantity=beverage_detail_map.get(ingr),
                    unit=None
                )
        return preparation_details

    def __str__(self):
        return "'beverage_type': '{beverage_type}', 'preparation_details':'{preparation_details}'".format(
            beverage_type=self.beverage_type,
            preparation_details=self.preparation_details
        )

    def __repr__(self):
        return "'beverage_type': '{beverage_type}', 'preparation_details':'{preparation_details}'".format(
            beverage_type=self.beverage_type,
            preparation_details=self.preparation_details
        )
