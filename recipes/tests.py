from django.test import TestCase
from .models import Recipe

# Create your tests here.
class RecipeModelTest(TestCase):
    def setUpTestData():
      Recipe.objects.create(name='Tea', ingredients='Water, Tea Leaves, Sugar', cooking_time=5)

    def test_recipe_name(self):
       recipe = Recipe.objects.get(id=1)
       field_label = recipe._meta.get_field('name').verbose_name
       self.assertEqual(field_label, 'name')

    def test_recipe_name_max_length(self):
       recipe = Recipe.objects.get(id=1)
       max_length = recipe._meta.get_field('name').max_length
       self.assertEqual(max_length, 120)

    def test_ingredients_max_length(self):
       recipe = Recipe.objects.get(id=1)
       max_length = recipe._meta.get_field('ingredients').max_length
       self.assertEqual(max_length, 350)

    def test_cooking_time_help(self):
       recipe = Recipe.objects.get(id=1)
       time_help = recipe._meta.get_field('cooking_time').help_text
       self.assertEqual(time_help, 'in minutes')
