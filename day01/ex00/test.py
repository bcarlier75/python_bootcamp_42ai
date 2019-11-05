from book import Book
from recipe import Recipe
import datetime

salad = Recipe(name='Salad', cooking_lvl=1, cooking_time=10, ingredients=['salad', 'Tomato', 'Ham'],
               description='A delicious salad.', recipe_type='lunch')
flan = Recipe(name='Flan', cooking_lvl=2, cooking_time=30, ingredients=['egg', 'milk', 'butter'],
              description='A delicious flan.', recipe_type='dessert')
choco = Recipe(name='Flanchoco', cooking_lvl=2, cooking_time=35, ingredients=['egg', 'milk', 'butter', 'chocolate'],
               description='A delicious flan au chocolat.', recipe_type='dessert')
Shouldnotwork = 'Shouldnotwork'

rcp_dict = dict.fromkeys(['starter', 'lunch', 'dessert'])
my_book = Book(name="Benji's book", last_update=datetime.datetime.now(),
               creation_date=datetime.datetime.now(), recipes_list=rcp_dict)
my_book.add_recipe(salad)
my_book.add_recipe(flan)
my_book.add_recipe(choco)
print('Three recipes added. Next one wont work.')
my_book.add_recipe(Shouldnotwork)  # should not work as it is not an instance of Recipe class
print()
print('---- Recipe for flan ----')
flanbis = my_book.get_recipe_by_name(flan)
print('---- Recipe for salad ----')
saladbis = my_book.get_recipe_by_name(salad)

print('---- Starter recipes ----')
starter_list = my_book.get_recipes_by_types('starter')
if starter_list is not None:
    if isinstance(starter_list, list):
        for elem in starter_list:
            print(str(elem))
    else:
        print(str(starter_list))

print('---- Lunch recipes ----')
lunch_list = my_book.get_recipes_by_types('lunch')
if lunch_list is not None:
    if isinstance(lunch_list, list):
        for elem in lunch_list:
            print(str(elem))
    else:
        print(str(lunch_list))

print('---- Dessert recipes ----')
dessert_list = my_book.get_recipes_by_types('dessert')
if dessert_list is not None:
    if isinstance(dessert_list, list):
        for elem in dessert_list:
            print(str(elem))
    else:
        print(str(dessert_list))
