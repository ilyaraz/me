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

def lb(x):
    return ur.lb * x

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

egg = Food('egg', 72, ct(1))
bobs_red_mill_old_fashioned_rolled_oats = Food('oatmeal', 190, cup(0.5))
chicken_breast = Food('chicken breast', 165, gr(100))
kirkland_cookies_cream_protein_bar = Food('protein bar', 180, ct(1))
pb_protein_bar = Food('protein bar', 190, ct(1))
green_lentils = Food('green lentils', 145, cup(0.25))
frozen_strawberries = Food('frozen strawberries', 50, gr(140))
pb2 = Food('PB2', 60, tbsp(2))
protein_powder_whey_isolate = Food('protein powder', 140, gr(39))
xanthan_gum = Food('xanthan gum', 5, tsp(0.5))
cashew_milk = Food('cashew milk', 25, cup(1))
sparkling_ice = Food('sparkling ice', 5, ml(500))
pop_corn = Food('pop corn', 400, ct(1))
pelmeni = Food('pelmeni', 150, ct(8))
abes = Food('abes', 200, ct(2))
sushi_rice = Food('sushi rice', 170, cup(0.25))
ramen = Food('ramen', 410, ct(1))
egg_whites = Food('egg whites', 25, tbsp(3))
gf_bread = Food('gluten-free bread', 180, ct(2))
banana = Food('banana', 89, gr(100))
potatoes = Food('potatoes', 77, gr(100))
sesame_oil = Food('sesame oil', 120, tbsp(1))
portobello = Food('portobellos', 22, gr(100))

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
    (sparkling_ice, ml(1000)),
    (pop_corn, ct(1)),
    (pelmeni, ct(3)),
    (abes, ct(1)),
    (abes, ct(1)),
    (abes, ct(2))
]

food[dt('2020-10-21')] = [
    (oatmeal, cup(0.75)),
    (egg, ct(4)),
    (pop_corn, ct(1)),
    (sparkling_ice, ml(1000)),
    (pop_corn, ct(1)),
    (sparkling_ice, ml(500)),
    (chicken_breast, gr(303)),
    (protein_bar, ct(1)),
    (sparkling_ice, ml(500)),
    (pb_protein_bar, ct(1)),
    (frozen_strawberries, gr(130)),
    (pb2, tbsp(2)),
    (protein_powder, gr(39)),
    (xanthan_gum, tsp(0.5)),
    (cashew_milk, cup(0.5)),
    (pop_corn, ct(1))
]

food[dt('2020-10-22')] = [
    (oatmeal, cup(0.75)),
    (egg, ct(4)),
    (pb_protein_bar, ct(1)),
    (pb_protein_bar, ct(1)),
    (chicken_breast, gr(270)),
    (sushi_rice, cup(0.75)),
    (pb_protein_bar, ct(1)),
    (sparkling_ice, ml(500)),
    (sparkling_ice, ml(500)),
    (sparkling_ice, ml(500)),
    (frozen_strawberries, gr(260)),
    (pb2, tbsp(4)),
    (protein_powder, gr(78)),
    (xanthan_gum, tsp(1.0)),
    (cashew_milk, cup(1.0)),
    (ramen, ct(1)),
    (sparkling_ice, ml(500)),
    (sparkling_ice, ml(500))
]

food[dt('2020-10-23')] = [
    (oatmeal, cup(0.75)),
    (egg, ct(4)),
    (egg_whites, tbsp(6)),
    (chicken_breast, gr(267)),
    (frozen_strawberries, gr(260)),
    (pb2, tbsp(4)),
    (protein_powder, gr(78)),
    (xanthan_gum, tsp(1.0)),
    (cashew_milk, cup(1.0)),
    (pb_protein_bar, ct(1)),
    (gf_bread, ct(2)),
    (gf_bread, ct(2)),
    (pb2, tbsp(4)),
    (banana, gr(124)),
    (gf_bread, ct(1)),
    (pb2, tbsp(2)),
    (banana, gr(120)),
    (gf_bread, ct(2))
]

food[dt('2020-10-24')] = [
    (egg, ct(4)),
    (egg_whites, tbsp(6)),
    (gf_bread, ct(1)),
    (pb2, tbsp(2)),
    (banana, gr(105)),
    (chicken_breast, gr(349)),
    (potatoes, gr(578)),
    (sesame_oil, tbsp(1)),
    (gf_bread, ct(1)),
    (pb2, tbsp(2)),
    (banana, gr(120)),
    (gf_bread, ct(1)),
    (frozen_strawberries, gr(260)),
    (pb2, tbsp(4)),
    (protein_powder, gr(78)),
    (xanthan_gum, tsp(1.0)),
    (cashew_milk, cup(1.0)),
    (banana, gr(106)),
    (gf_bread, ct(1))
]

food[dt('2020-10-25')] = [
    (egg, ct(4)),
    (egg_whites, tbsp(6)),
    (gf_bread, ct(1)),
    (pb2, tbsp(2)),
    (banana, gr(156)),
    (Food('eat out', 650, ct(1)), ct(1)),
    (potatoes, gr(666)),
    (sesame_oil, tbsp(1)),
    (chicken_breast, gr(240)),
    (portobello, gr(170)),
    (gf_bread, ct(3)),
    (pb2, tbsp(2)),
    (banana, gr(153))
]

gf_bread = Food('gluten-free bread', 80, ct(1))
pb_protein_powder = Food('pb protein powder', 130, ct(1))
popcorn = Food('popcorn', 130 * 2.5, ct(1)) 

food[dt('2020-10-26')] = [
    (egg, ct(4)),
    (egg_whites, tbsp(6)),
    (gf_bread, ct(1)),
    (pb2, tbsp(2)),
    (banana, gr(150)),
    (pb_protein_powder, ct(2)),
    (banana, gr(300)),
    (popcorn, ct(1)),
    (cashew_milk, cup(1.5)),
    (sushi_rice, cup(0.75)),
    (sesame_oil, tbsp(1)),
    (Food('eat out', 400, ct(1)), ct(1))
]

food[dt('2020-10-27')] = [
    (banana, gr(324)),
    (pb_protein_powder, ct(1)),
    (cashew_milk, cup(1.5)),
    (pb2, tbsp(2)),
    (popcorn, ct(1)),
    (gf_bread, ct(1)),
    (pb2, tbsp(2)),
    (banana, gr(153)),
    (sushi_rice, cup(0.75)),
    (sesame_oil, tbsp(1)),
    (pb_protein_powder, ct(2)),
    (popcorn, ct(1)),
    (pb_protein_bar, ct(2)),
    (cashew_milk, cup(1.5)),
    (pb_protein_powder, ct(1))
]

ribeye_steak = Food('ribeye steak', 1320, lb(1))

food[dt('2020-10-28')] = [
    (banana, gr(286)),
    (pb_protein_powder, ct(1)),
    (cashew_milk, cup(1)),
    (pb2, tbsp(2)),
    (gf_bread, ct(1)),
    (pb2, tbsp(2)),
    (banana, gr(136)),
    (popcorn, ct(1)),
    (pb_protein_bar, ct(1)),
    (sushi_rice, cup(0.75)),
    (sesame_oil, tbsp(1)),
    (Food('plane snacks', 200, ct(1)), ct(1)),
    (protein_bar, ct(1)),
    (ribeye_steak, lb(0.5))
]

avocado = Food('avocado', 160, gr(100))
bacon = Food('bacon', 90, ct(2))
tj_marinated_thighs = Food('TJ marinated thighs', 140, gr(112))
walnuts = Food('walnuts', 200, gr(30))

food[dt('2020-11-02')] = [
    (egg, ct(4)),
    (egg_whites, tbsp(6)),
    (bacon, ct(3)),
    (avocado, gr(68)),
    (tj_marinated_thighs, gr(425)),
    (pb_protein_powder, ct(2)),
    (cashew_milk, cup(2.5)),
    (walnuts, gr(30)),
    (frozen_strawberries, gr(260)),
    (pb2, tbsp(4)),
    (pb_protein_powder, ct(2)),
    (xanthan_gum, tsp(1)),
    (cashew_milk, cup(1)),
    (avocado, gr(71)),
    (bacon, ct(4)),
    (pb_protein_bar, ct(2))
]

tj_marinated_breasts = Food('TJ marinated breasts', 130, gr(112))

food[dt('2020-11-03')] = [
    (egg, ct(4)),
    (bacon, ct(4)),
    (pb_protein_powder, ct(1)),
    (cashew_milk, cup(1.5)),
    (protein_bar, ct(1)),
    (frozen_strawberries, gr(260)),
    (pb2, tbsp(4)),
    (pb_protein_powder, ct(2)),
    (xanthan_gum, tsp(1)),
    (cashew_milk, cup(1)),
    (tj_marinated_breasts, gr(431)),
    (protein_bar, ct(2)),
    (avocado, gr(177)),
    (protein_bar, ct(1)),
    (walnuts, gr(30)),
    (bacon, ct(3))
]

bacon = Food('bacon', 90, ct(2))
cream_cheese = Food('cream cheese', 80, gr(30))
peanut_butter = Food('peanut butter', 220, tbsp(2))

food[dt('2020-11-04')] = [
    (egg, ct(4)),
    (bacon, ct(4)),
    (avocado, gr(114)),
    (protein_bar, ct(3)),
    (tj_marinated_breasts, gr(475)),
    (protein_bar, ct(1)),
    (cream_cheese, gr(115)),
    (peanut_butter, cup(0.25)),
    (protein_bar, ct(1))
]

bacon = Food('bacon', 50, ct(2))

food[dt('2020-11-05')] = [
    (egg, ct(4)),
    (bacon, ct(4)),
    (avocado, gr(142)),
    (protein_bar, ct(1)),
    (cream_cheese, gr(115)),
    (peanut_butter, cup(0.25)),
    (tj_marinated_breasts, gr(517)),
    (cream_cheese, gr(115)),
    (peanut_butter, cup(0.25))
]

salami = Food('salami', 600, gr(170))

food[dt('2020-11-06')] = [
    (egg, ct(4)),
    (bacon, ct(6)),
    (avocado, gr(143)),
    (tj_marinated_breasts, gr(396)),
    (cream_cheese, gr(115)),
    (peanut_butter, cup(0.25)),
    (cream_cheese, gr(115)),
    (peanut_butter, cup(0.25)),
    (protein_bar, ct(1)),
    (salami, gr(170)),
    (pb_protein_powder, ct(1)),
    (cashew_milk, cup(1.5))
]

heavy_cream = Food('heavy cream', 50, tbsp(1))

food[dt('2020-11-07')] = [
    (egg, ct(4)),
    (bacon, ct(6)),
    (avocado, gr(123)),
    (protein_bar, ct(1)),
    (tj_marinated_breasts, gr(425)),
    (cream_cheese, gr(115)),
    (peanut_butter, cup(0.25)),
    (cream_cheese, gr(97)),
    (peanut_butter, cup(0.25)),
    (Food('eat out', 500, ct(1)), ct(1)),
    (heavy_cream, tbsp(2)),
    (protein_bar, ct(1)),
]

butter = Food('butter', 100, tbsp(1))
medium_cheddar = Food('medium sharp cheddar', 120, gr(30))
brie = Food('brie', 110, gr(28))

food[dt('2020-11-08')] = [
    (heavy_cream, tbsp(2)),
    (butter, tbsp(1)),
    (tj_marinated_breasts, gr(506)),
    (avocado, gr(123)),
    (sesame_oil, tbsp(1)),
    (medium_cheddar, gr(89)),
    (heavy_cream, tbsp(2)),
    (cream_cheese, gr(115)),
    (peanut_butter, cup(0.25)),
    (medium_cheddar, gr(50)),
    (protein_bar, ct(1)),
    (brie, gr(36)),
    (brie, gr(28)),
]

bacon = Food('bacon', 60, ct(2))

food[dt('2020-11-09')] = [
    (heavy_cream, tbsp(2)),
    (avocado, gr(137)),
    (brie, gr(65)),
    (bacon, ct(6)),
    (egg, ct(4)),
    (tj_marinated_breasts, gr(425)),
    (cream_cheese, gr(115)),
    (peanut_butter, cup(0.25)),
    (brie, gr(83)),
    (medium_cheddar, gr(127)),
    (protein_bar, ct(1)),
    (protein_bar, ct(1)),
]

food[dt('2020-11-10')] = [
    (avocado, gr(122)),
    (egg, ct(4)),
    (protein_bar, ct(2)),
    (tj_marinated_breasts, gr(407)),
    (sesame_oil, tbsp(1)),
    (cream_cheese, gr(115)),
    (peanut_butter, cup(0.25)),
    (protein_bar, ct(1)),
    (avocado, gr(120)),
    (Food('salami', 190, ct(8)), ct(8)),
    (walnuts, gr(30)),
    (bacon, ct(4))
]

bacon = Food('bacon', 80, ct(2))
cheese = Food('cheese', 110, gr(28))

food[dt('2020-11-11')] = [
    (bacon, ct(4)),
    (egg, ct(3)),
    (butter, tbsp(2.25)),
    (heavy_cream, tbsp(2)),
    (heavy_cream, tbsp(2)),
    (tj_marinated_breasts, gr(507)),
    (sesame_oil, tbsp(1)),
    (cream_cheese, gr(115)),
    (peanut_butter, cup(0.25)),
    (heavy_cream, tbsp(2)),
    (cheese, gr(220)),
    (pb_protein_bar, ct(2)),
]

food[dt('2020-11-12')] = [
    (bacon, ct(4)),
    (egg, ct(4)),
    (avocado, gr(150)),
    (cheese, gr(34)),
    (tj_marinated_breasts, gr(395)),
    (sesame_oil, tbsp(1)),
    (cream_cheese, gr(115)),
    (peanut_butter, cup(0.25)),
    (heavy_cream, tbsp(2)),
    (pb_protein_bar, ct(2)),
]

food[dt('2020-11-13')] = [
    (bacon, ct(4)),
    (avocado, gr(147)),
    (tj_marinated_breasts, gr(475)),
    (cream_cheese, gr(115)),
    (peanut_butter, cup(0.25)),
    (cream_cheese, gr(115)),
    (peanut_butter, cup(0.25)),
    (walnuts, gr(30)),
    (bacon, ct(4)),
]

food[dt('2020-11-14')] = [
    (bacon, ct(6)),
    (avocado, gr(147)),
    (egg, ct(4)),
    (heavy_cream, tbsp(2)),
    (cream_cheese, gr(115)),
    (peanut_butter, cup(0.25)),
    (tj_marinated_breasts, gr(475)),
    (ribeye_steak, lb(0.5)),
    (bacon, ct(1)),
]

apple = Food('apple', 52, gr(100))
casein_powder = Food('casein powder', 120, ct(1))
popcorn = Food('pop corn', 400, ct(1))

food[dt('2020-11-15')] = [
    (banana, gr(131)),
    (bacon, ct(6)),
    (avocado, gr(123)),
    (egg, ct(4)),
    (apple, gr(272)),
    (tj_marinated_breasts, gr(399)),
    (casein_powder, ct(1)),
    (cashew_milk, cup(1.5)),
    (frozen_strawberries, gr(260)),
    (pb2, tbsp(4)),
    (protein_powder, gr(78)),
    (xanthan_gum, tsp(1.0)),
    (cashew_milk, cup(1.0)),
    (popcorn, ct(1)),
    (pb2, tbsp(2)),
    (gf_bread, ct(1)),
    (banana, gr(70)),
    (banana, gr(68)),
]

chocolate = Food('chocolate', 60, ct(1))

food[dt('2020-11-16')] = [
    (tj_marinated_breasts, gr(503)),
    (apple, gr(202)),
    (banana, gr(133)),
    (pb2, tbsp(2)),
    (gf_bread, ct(1)),
    (frozen_strawberries, gr(260)),
    (pb2, tbsp(4)),
    (protein_powder, gr(78)),
    (xanthan_gum, tsp(1.0)),
    (cashew_milk, cup(1.0)),
    (casein_powder, ct(2)),
    (cashew_milk, cup(3)),
    (bacon, ct(6)),
    (egg, ct(4)),
    (chocolate, ct(1)),
    (apple, gr(200)),
    (pb_protein_bar, ct(1)),
]

food[dt('2020-11-17')] = [
    (banana, gr(123)),
    (tj_marinated_breasts, gr(430)),
]

count_calories(food)
