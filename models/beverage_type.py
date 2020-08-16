from enum import Enum

'''
Enum for the name of the beverages that the machines can prepare
'''
class BeverageType(Enum):
    HOT_TEA = "hot_tea"
    HOT_COFFEE = "hot_coffee"
    BLACK_TEA = "black_tea"
    GREEN_TEA = "green_tea"

    @staticmethod
    def get_values():
        return list(map(lambda c: c.value, BeverageType))
