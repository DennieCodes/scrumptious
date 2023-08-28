from django.contrib import admin
from recipes.models import Recipe, RecipeStep, Ingredients

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "id",
    )

@admin.register(RecipeStep)
class RecipeStepAdmin(admin.ModelAdmin):
    list_display = (
        "instruction",
        "order",
        "id"
    )

@admin.register(Ingredients)
class IngredientsAdmin(admin.ModelAdmin):
    list_display = (
        "amount",
        "food_item"
    )