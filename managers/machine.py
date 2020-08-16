from exceptions.invalid_ingredient_exception import InvalidIngredientException
from exceptions.invalid_beverage_exception import InvalidBeverageException
from exceptions.unavailable_ingredient_exception import UnavailableIngredientException
from exceptions.insufficient_ingredient_exception import InsufficientIngredientException
from exceptions.invalid_outlet_exception import InvalidOutletException
from models.ingredient import Ingredient
from models.ingredient_holder import IngredientHolder
from models.outlet import Outlet
from models.beverage import Beverage
import threading

# Would have liked to break this class into machine model and operator manager
class Machine():
    def __init__(self, *args, **kwargs):
        self.lock = threading.Lock()
        self.outlets = self.create_outlets(kwargs.get("num_outlets"))
        self.ingredient_map = self.load_ingredients(kwargs.get("total_items_quantity"))
        self.beverages_map = self.load_beverages(kwargs.get("beverages"))

    ######################## init methods start ######################
    def load_ingredients(self, ingredient_quantity_map):
        ingredient_map = {}
        for ingr in ingredient_quantity_map:
            if ingr not in Ingredient.get_values():
                raise InvalidIngredientException(ingr, Ingredient.get_values())
            else:
                ingredient_map[ingr] = IngredientHolder(
                    ingredient_type=ingr,
                    quantity=ingredient_quantity_map.get(ingr),
                    unit=None
                )
        return ingredient_map

    def create_outlets(self, num_outlets):
        outlets = []
        for i in range(num_outlets):
            outlets.append(Outlet(id=str(i + 1)))
        return outlets

    def load_beverages(self, beverage_detail_map):
        beverages_map = {}
        for beverage in beverage_detail_map:
            beverages_map[beverage] = Beverage(
                beverage_type=beverage,
                preparation_details=beverage_detail_map.get(beverage)
            )

        return beverages_map

    ######################## init methods end ######################

    ######################## public methods ########################

    """
    This method is used to pour a beverage from any of the outlets
    """
    def dispense(self, beverage):
        if beverage not in self.beverages_map:
            raise InvalidBeverageException(beverage, self.beverages_map.keys())

        processed = False
        for outlet in self.outlets:
            try:
                self.dispenseFromOutlet(outlet, beverage)
                processed = True
                break
            except InvalidOutletException as e:
                print(e)
        if not processed:
            print("Failed to prepare {} as no valid outlet".format(beverage))

    """
    This method is used to pour a beverage from any of the outlets

    This will start the outlet, try to prepare the bevarage and then close the outlet
    """
    def dispenseFromOutlet(self, outlet, beverage):
        outlet.start()
        try:
            self.prepare_beverage(self.beverages_map.get(beverage))
            print("{beverage} is prepared".format(beverage=beverage))
        except UnavailableIngredientException as e:
            print(e)
        except InsufficientIngredientException as e:
            print(e)
        finally:
            outlet.stop()


    def load(self, ingredient_type, quantity):
        if ingredient_type not in Ingredient.get_values():
            raise InvalidIngredientException(ingr, Ingredient.get_values())

        if ingredient_type not in self.ingredient_map:
            self.ingredient_map[ingredient_type] = IngredientHolder(
                ingredient_type=ingredient_type,
                quantity=quantity,
                unit=None
            )
        else:
            ## Added lock to make edits thread safe
            with self.lock:
                self.ingredient_map[ingredient_type].load(quantity)

    ############################ Private Methods #####################

    """
    This method is used to prepare the input beverage

    Checks for 2 errors:
    - UnavailableIngredientException
    - InsufficientIngredientException
    """
    def prepare_beverage(self, beverage_obj):
        diff = set(beverage_obj.preparation_details.keys()).difference(set(self.ingredient_map.keys()))
        if diff:
            raise UnavailableIngredientException(beverage_obj.beverage_type, list(diff)[0])
        ## Added lock to make edits thread safe
        with self.lock:
            for ingr in beverage_obj.preparation_details:
                if self.ingredient_map.get(ingr) < beverage_obj.preparation_details.get(ingr):
                    raise InsufficientIngredientException(beverage_obj.beverage_type, ingr)
            for ingr in beverage_obj.preparation_details:
                self.ingredient_map.get(ingr).subtract(beverage_obj.preparation_details.get(ingr))
