from django.db import models
from django.conf import settings

# Recipe Model
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    picture = models.URLField(blank = True)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="recipes",
        on_delete=models.CASCADE,
        null=True
    )

# RecipeStep Model
class RecipeStep(models.Model):
    instruction = models.TextField()
    order = models.PositiveIntegerField()
    recipe = models.ForeignKey(
        "Recipe",
        related_name="steps",
        on_delete=models.CASCADE
    )

    def recipe_title(self):
        return self.recipe.title

    class Meta:
        ordering = ['order']

# Ingredients Model
class Ingredients(models.Model):
    amount = models.CharField(max_length=100)
    food_item = models.CharField(max_length=100)
    recipe = models.ForeignKey(
        "Recipe",
        related_name="ingredients",
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["food_item"]
