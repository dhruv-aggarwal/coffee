from enum import Enum

'''
Enum for the names of the allowed ingredients
'''
class Ingredient(Enum):
    HOT_WATER = "hot_water"
    HOT_MILK = "hot_milk"
    GINGER_SYRUP = "ginger_syrup"
    SUGAR_SYRUP = "sugar_syrup"
    TEA_LEAVES_SYRUP = "tea_leaves_syrup"
    GREEN_MIXTURE = "green_mixture"

    @staticmethod
    def get_values():
        return list(map(lambda c: c.value, Ingredient))
