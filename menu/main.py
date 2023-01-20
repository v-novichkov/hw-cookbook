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
        pprint(cookbook)



get_menu('Recipes.txt')