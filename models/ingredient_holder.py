from .quantity_unit import QuantityUnit
import threading


'''
Class to define the container for the ingredient
'''
class IngredientHolder():
    def __init__(self, *args, **kwargs):
        self.lock = threading.Lock()
        self.ingredient_type = kwargs.get("ingredient_type")
        self.quantity = kwargs.get("quantity")
        self.unit = kwargs.get("unit")
        if not self.unit:
            self.unit = QuantityUnit.ML

    def __str__(self):
        return "'ingredient_type': '{}', 'quantity':'{}', 'unit': '{}'".format(
            self.ingredient_type, self.quantity, self.unit
        )

    def __repr__(self):
        return "'ingredient_type': '{ingredient_type}', 'quantity':'{quantity}', 'unit': '{unit}'".format(
            ingredient_type=self.ingredient_type,
            quantity=self.quantity,
            unit=self.unit
        )

    def __gt__(self, holder2):
        return self.quantity > holder2.quantity

    ## To subtract the quantity
    def subtract(self, holder2):
        with self.lock:
            if self.__gt__(holder2):
                self.quantity = self.quantity - holder2.quantity

    ## To add the quantity
    def load(self, quantity):
        with self.lock:
            if quantity > 0:
                self.quantity = self.quantity + quantity
