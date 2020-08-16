from data.test_data import *
from managers.machine import Machine
from models.beverage_type import BeverageType
from multiprocessing import Pool, Process


m = Machine(
    num_outlets=BASE_TEST["machine"]["outlets"]["count_n"],
    total_items_quantity=BASE_TEST["machine"]["total_items_quantity"],
    beverages=BASE_TEST["machine"]["beverages"]
)

## Try creating all the beverages
for beverage in BeverageType.get_values():
    m.dispense(beverage)

## No outlets
m2 = Machine(
    num_outlets=BASE_TEST_2["machine"]["outlets"]["count_n"],
    total_items_quantity=BASE_TEST_2["machine"]["total_items_quantity"],
    beverages=BASE_TEST_2["machine"]["beverages"]
)

## Try creating all the beverages
for beverage in BeverageType.get_values():
    m2.dispense(beverage)


## One ingredient not present
m3 = Machine(
    num_outlets=BASE_TEST_3["machine"]["outlets"]["count_n"],
    total_items_quantity=BASE_TEST_3["machine"]["total_items_quantity"],
    beverages=BASE_TEST_3["machine"]["beverages"]
)

## Try creating all the beverages
for beverage in BeverageType.get_values():
    m3.dispense(beverage)

## Load that ingredient
m3.load("hot_water", 400)

for beverage in BeverageType.get_values():
    m3.dispense(beverage)

"""
To be added:
- Test cases to check availability of outlets
"""
