class InvalidBeverageException(Exception):
    def __init__(self, beverage, allowed_values):
        super().__init__("Input beverage {beverage} is not in the allowed_values {allowed_values}".format(
            beverage=beverage,
            allowed_values=allowed_values
        ))
