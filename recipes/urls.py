from django.urls import path
from recipes.views import show_recipe, recipe_list, create_recipe, update_recipe, delete_recipe

urlpatterns = [
    path("recipes/create/", create_recipe, name="create_recipe"),
    path("recipes/", recipe_list, name="recipe_list"),
    path("recipes/<int:id>/", show_recipe, name="show_recipe"),
    path("recipes/<int:id>/update", update_recipe, name="update_recipe"),
    path("recipes/<int:id>/delete", delete_recipe, name="delete_recipe")
]