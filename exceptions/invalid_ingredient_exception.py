class InvalidIngredientException(Exception):
    def __init__(self, ingredient_name, allowed_values):
        super().__init__("Input ingredient {ingredient_name} is not in the allowed_values {allowed_values}".format(
            ingredient_name=ingredient_name,
            allowed_values=allowed_values
        ))
