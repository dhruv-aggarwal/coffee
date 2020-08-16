class InsufficientIngredientException(Exception):
    def __init__(self, beverage, ingredient):
        super().__init__("{beverage} cannot be prepared because item {ingredient} is not sufficient".format(
            beverage=beverage,
            ingredient=ingredient
        ))
