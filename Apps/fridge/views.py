import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import *

# Create your class-based views here.


@login_required()
def home(request):
    fridge = Fridge.objects.filter(user=request.user)
    context = {
        'fridge': fridge,
    }
    return render(request, 'fridge/home.html', context)


class FridgeDetailView(DetailView):
    model = Fridge


# CREATE ITEM
class FridgeCreateView(LoginRequiredMixin, CreateView):
    model = Fridge
    fields = ['name', 'quantity']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# UPDATE ITEM
class FridgeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Fridge
    # When successfully deleted, will take user back to homepage
    success_url = '/fridge'
    fields = ['name', 'quantity']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        fridge_item = self.get_object()
        # Prevents others to update other people's items
        if self.request.user == fridge_item.user:
            return True
        return False


class FridgeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Fridge
    # When successfully deleted, will take user back to homepage
    success_url = '/fridge'

    def test_func(self):
        fridge_item = self.get_object()
        # Prevents others to update other people's items
        if self.request.user == fridge_item.user:
            return True
        return False


@login_required()
def recipe(request):
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/random"

    querystring = {
        'number': 1,
        'veryPopular': True,
        'fillIngredients': True,
        'addRecipeInformation': True,
        'addRecipeNutrition': True
    }

    headers = {
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        'x-rapidapi-key': "f8540d734amsh0d72a908c3766d4p1be29fjsn28baee86ebe6"
    }

    res = requests.request("GET", url, headers=headers, params=querystring).json()['recipes']

    instructions = get_instructions(res[0]['analyzedInstructions'])
    ingredients = get_ingredients(res[0]['extendedIngredients'])

    context = {
        'title': res[0]['title'],
        'instructions': instructions,
        'ingredients': ingredients,
        'recipe_link': res[0]['sourceUrl'],
        'image_link': res[0]['image'],
    }

    print(res[0]['summary'])

    return render(request, 'fridge/fridge_recipe.html', context)


def get_instructions(res: list) -> list:
    instructions = []

    for instruction in res[0]['steps']:
        instructions.append(instruction['step'])

    return instructions


def get_ingredients(res: list) -> list:
    ingredients = []

    for ingredient in res:
        ingredients.append(ingredient['name'])

    return ingredients
