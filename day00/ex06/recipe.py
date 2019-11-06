sandwich = {'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'], 'meal': 'lunch', 'prep_time': 10}
cake = {'ingredients': ['flour', 'sugar', 'egg'], 'meal': 'dessert', 'prep_time': 60}
salad = {'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'], 'meal': 'lunch', 'prep_time': 15}
cookbook = {'sandwich': sandwich, 'cake': cake, 'salad': salad}


def print_recipe(recipe_name: str):
    try:
        print(f'Recipe for {recipe_name}:\n'
              f'\tIngredients list: {cookbook[recipe_name]["ingredients"]}\n'
              f'\tTo be eaten for {cookbook[recipe_name]["meal"]}.\n'
              f'\tTakes {cookbook[recipe_name]["prep_time"]} minute(s) of cooking.')
    except ValueError:
        pass


def print_cookbook(my_dict: dict):
    for key, value in my_dict.items():
        print(f'{key}: {value}')


def del_recipe(recipe_name: str):
    try:
        del cookbook[recipe_name]
        print(f'Recipe {recipe_name} deleted.')
    except KeyError:
        print("Recipe's name isn't in the cookbook.")


def add_recipe(recipe_name: str, ingredients: list, meal: str, prep_time: int):
    cookbook[recipe_name] = {'ingredients': ingredients, 'meal': meal, 'prep_time': prep_time}


def main():
    while True:
        num_input = input(f'Please select an option by typing the corresponding number:\n'
                          f'1: Add a recipe\n'
                          f'2: Delete a recipe\n'
                          f'3: Print a recipe\n'
                          f'4: Print the cookbook\n'
                          f'5: Quit\n')
        num_input = int(num_input)
        if isinstance(num_input, int):
            if num_input == 1:
                recipe_name = input(f"Please enter the recipe's name: ")
                ingredients = input(f"Please enter the ingredients separated by spaces: ")
                try:
                    ingredients = list(ingredients.split())
                except ValueError:
                    print(f'Wrong format for ingredients.')
                    return
                meal = input(f"Please enter the meal type: ")
                prep_time = input(f"Please enter the preparation time: ")
                prep_time = int(prep_time)
                if not isinstance(prep_time, int):
                    print(f'Wrong format for preparation time.')
                    return
                add_recipe(recipe_name, ingredients, meal, prep_time)
            elif num_input == 2:
                recipe_name = input(f"Please enter the recipe's name: ")
                del_recipe(recipe_name)
            elif num_input == 3:
                recipe_name = input(f"Please enter the recipe's name to get its details: ")
                print_recipe(recipe_name)
            elif num_input == 4:
                print_cookbook(cookbook)
            elif num_input == 5:
                return
            else:
                print(f'This option does not exist, please type the corresponding number.\nTo exit, enter 5.')
        else:
            print(f'This option does not exist, please type the corresponding number.\nTo exit, enter 5.')


if __name__ == '__main__':
    main()
