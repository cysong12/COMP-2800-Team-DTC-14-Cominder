from Cominder.users.reminder_feature_temp import User
from enum import Enum
import datetime
import requests
import json

'''
Rough snippet for the fridge feature.
To be implemented/moved in views.py
'''


class Fridge:
    def __init__(self, **kwargs):
        self.__items_dict = {}
        self.add_items(**kwargs)

    def get_items_dict(self):
        return self.__items_dict

    def get_number_of_an_item(self, item_name):
        return self.__items_dict[item_name]

    def add_items(self, **kwargs):
        for key in kwargs.keys():
            try:
                self.__items_dict[key] += kwargs[key]
            except KeyError:
                self.__items_dict[key] = kwargs[key]

    def subtract_items(self, **kwargs):
        for key in kwargs.keys():
            try:
                self.__items_dict[key] -= kwargs[key]
            except KeyError:
                return "Item doesn't exist."
            else:
                if self.__items_dict[key] <= 0:
                    del self.__items_dict[key]

    def delete_items(self, args):
        for item in args:
            try:
                del self.__items_dict[item]
            except KeyError:
                return "Item doesn't exist."


class Recipes:
    def __init__(self, intolerance: list, ingredients: list = None):
        self.__intolerance = intolerance
        self.__ingredients = ingredients if ingredients is not None else ''

    def generate_recipe(self, ingredients: list = None):
        api_key = "80606778f33c4f65b713ee014ecd2f70"
        url = "https://api.spoonacular.com/recipes/complexSearch"
        api_url = f"{url}?apiKey={api_key}"
        parameters = {
            'number': 5,
            'includeIngredients': ', '.join(ingredients) if ingredients is not None else self.__ingredients,
            'intolerances': ', '.join(self.__intolerance) if not self.__intolerance else '',
            'fillIngredients': True,
            'addRecipeInformation': True,
            'addRecipeNutrition': True
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': api_key
        }

        res = requests.get(api_url, params=parameters, headers=headers)
        data = res.json()
        return data


# test
def main():
    user = User('Choi', 'Song', datetime.datetime(1992, 12, 18), True, middle_name="Yong")
    user_fridge = Fridge(bananas=5, apples=3, grapes=1)
    print(user_fridge.get_items_dict())
    user_fridge.add_items(oranges=2, watermelon=10)
    print(user_fridge.get_items_dict())
    user_fridge.subtract_items(watermelon=5, apples=4)
    print(user_fridge.get_items_dict())
    user_fridge.delete_items(('grapes', 'oranges'))
    print(user_fridge.get_items_dict())
    print(user_fridge.get_number_of_an_item("bananas"))
    generate_recipe = Recipes(user.get_food_intolerance(), list(user_fridge.get_items_dict().keys()))
<<<<<<< HEAD
    recipe_json = generate_recipe.generate_recipe(list(user_fridge.get_items_dict().keys()))
    print(recipe_json)
    print('\n' + '-' * 100 + '\n')
    for k in recipe_json['results']:
        # print(list(k.keys()))
        print("Ingredients that are in the fridge:")
        for x in k['usedIngredients']:
            print(x['name'])
        print("Missing ingredients:")
        for x in k['missedIngredients']:
            print(x['name'])
        print("\n\nInstructions\n\n")
        counter = 1
        for x in k['analyzedInstructions']:
            for step in x['steps'][:-2]:
                print(f"{counter}: {step['step']}")
                counter += 1
        print(k['image'])
        print(k['sourceUrl'])
=======
    print(generate_recipe.generate_recipe(list(user_fridge.get_items_dict().keys())))
>>>>>>> dev


if __name__ == "__main__":
    main()
