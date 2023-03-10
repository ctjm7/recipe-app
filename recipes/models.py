from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=120)
    cooking_time = models.PositiveIntegerField(help_text='in minutes')
    ingredients = models.CharField(max_length=350)

    def calculate_difficulty(self):
      ingredients = self.ingredients.split(', ')
      if self.cooking_time < 10 and len(ingredients) < 4:
        difficulty = 'Easy'
      elif self.cooking_time < 10 and len(ingredients) >= 4:
        difficulty = 'Medium'
      elif self.cooking_time >= 10 and len(ingredients) < 4:
        difficulty = 'Intermediate'
      elif self.cooking_time >= 10 and len(ingredients) >=4:
        difficulty = 'Hard'
      return difficulty

    def __str__(self):
      return str(self.name)
