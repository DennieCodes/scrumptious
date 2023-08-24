from django.shortcuts import render, get_object_or_404, redirect
from recipes.models import Recipe
from recipes.forms import RecipeForm

# UPDATE RECIPE
def update_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)

    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('show_recipe', id=id)
    else:
        form = RecipeForm(instance=recipe)

    context = {
        'recipe': recipe,
        'form': form
    }
    return render(request, "recipes/update.html", context)

# CREATE RECIPE
def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()

    context = {
        'form': form,
    }

    return render(request, 'recipes/create.html', context)

# SHOW RECIPE
def show_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    context = {
        "recipe_object": recipe
    }
    return render(request, "recipes/detail.html", context)

# SHOW ALL RECIPES
def recipe_list(request):
    recipes = Recipe.objects.all()
    context = {
        "recipe_list": recipes,
    }
    return render(request, "recipes/list.html", context)

# DELETE RECIPE
def delete_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)

    recipe.delete()
    return redirect('recipe_list')