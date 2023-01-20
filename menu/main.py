import os

def get_menu(file):
    with open(file) as file:
        cookbook = dict()
        for line in file:
            dinner_name = line.strip()
            prod_count = int(file.readline())

            temp_list = []
            for item in range(prod_count):
                prod, quantity, unit = file.readline().split()
                temp_list.append(
                    {'Продукт': prod, 'Количество': quantity, 'Ед. измерения': unit}
                )
            cookbook[dinner_name] = temp_list
        print(cookbook)



get_menu(Recipes.txt)