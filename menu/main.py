import os
from pprint import pprint
def get_menu(file):
    with open(file, encoding="utf-8") as file:
        cookbook = dict()
        for line in file:
            dinner_name = line.strip()
            prod_count = int(file.readline())

            temp_list = []
            for item in range(prod_count):
                prod, quantity, unit = file.readline().split('|')
                temp_list.append(
                    {'Продукт': prod.strip(), 'Количество': quantity.strip(), 'Ед. измерения': unit.strip()}
                )
            cookbook[dinner_name] = temp_list

            file.readline()
        return cookbook



def get_shop_list_by_dishes(dishes, person_count):
    wishlist = {}
    for dish in cookbook:
       for dish_order in dishes:
            if dish_order == dish:
                for x in cookbook[dish]:
                    prod, quantity, unit = x.values()
                    if prod in wishlist.keys():
                        wishlist[prod]['Количество'] = int(wishlist[prod]['Количество']) + int(quantity)*int(person_count)
                    else:
                        count_prod = {'Количество': int(quantity)*int(person_count), 'Ед. измерения': unit}
                        wishlist.setdefault(prod, count_prod)
    pprint(wishlist)
    return wishlist


cookbook = get_menu('Recipes.txt')
pprint(cookbook)
get_shop_list_by_dishes(['Фахитос', 'Омлет'], '2')
