import pint
import datetime
from dataclasses import dataclass

ur = pint.UnitRegistry()

def cup(x):
    return ur.cup * x

def ct(x):
    return ur.count * x

def gr(x):
    return ur.gram * x

def tbsp(x):
    return ur.tablespoon * x

def tsp(x):
    return ur.teaspoon * x

def ml(x):
    return ur.ml * x

def dt(x):
    return datetime.datetime.strptime(x, '%Y-%m-%d')

@dataclass
class Food:
    name: str
    calories: float
    amount: pint.Quantity

def count_calories(food):
    for day in sorted(food.keys()):
        print(day.date())
        total = 0.0
        for (food_item, amount) in food[day]:
            calories = food_item.calories * amount / food_item.amount
            print(food_item.name, float(calories))
            total += calories
        print('Total: {}'.format(float(total)))

egg = Food('egg', 80, ct(1))
bobs_red_mill_old_fashioned_rolled_oats = Food('oatmeal', 180, cup(0.5))
chicken_breast = Food('chicken breast', 165, gr(100))
kirkland_cookies_cream_protein_bar = Food('protein bar', 180, ct(1))
green_lentils = Food('green lentils', 145, cup(0.25))
frozen_strawberries = Food('frozen strawberries', 50, gr(140))
pb2 = Food('PB2', 60, tbsp(2))
protein_powder_whey_isolate = Food('protein powder', 140, gr(39))
xanthan_gum = Food('xanthan gum', 5, tsp(0.5))
cashew_milk = Food('cashew milk', 25, cup(1))
sparkling_ice = Food('sparkling ice', 5, ml(500))

food = {}

oatmeal = bobs_red_mill_old_fashioned_rolled_oats
protein_bar = kirkland_cookies_cream_protein_bar
lentils = green_lentils
protein_powder = protein_powder_whey_isolate

food[dt('2020-10-20')] = [
    (oatmeal, cup(0.75)),
    (egg, ct(4)),
    (chicken_breast, gr(227)),
    (protein_bar, ct(1)),
    (lentils, cup(0.75)),
    (frozen_strawberries, gr(130)),
    (pb2, tbsp(2)),
    (protein_powder, gr(39)),
    (xanthan_gum, tsp(0.5)),
    (cashew_milk, cup(0.5)),
    (sparkling_ice, ml(1000)),
    (protein_bar, ct(2)),
    (sparkling_ice, ml(1000))
]

count_calories(food)
