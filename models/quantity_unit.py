from enum import Enum

class QuantityUnit(Enum):
    ML = "ml"

    @staticmethod
    def get_values():
        return list(map(lambda c: c.value, QuantityUnit))
