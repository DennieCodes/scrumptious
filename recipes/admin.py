from django.contrib import admin
from recipes.models import Recipe, RecipeStep

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "id",
    )

@admin.register(RecipeStep)
class RecipeStepAdmin(admin.ModelAdmin):
    list_display = (
        "recipe_title",
        "order",
        "id"
    )