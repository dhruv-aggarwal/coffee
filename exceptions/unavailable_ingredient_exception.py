class UnavailableIngredientException(Exception):
    def __init__(self, beverage, ingredient):
        super().__init__("{beverage} cannot be prepared because {ingredient} is not available".format(
            beverage=beverage,
            ingredient=ingredient
        ))
