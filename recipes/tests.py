from django.test import TestCase
from .models import Recipe
from .forms import RecipeSearchForm

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

    def test_get_absolute_url(self):
       recipe = Recipe.objects.get(id=1)
       self.assertEqual(recipe.get_absolute_url(), '/list/1')

    def test_calculate_difficulty(self):
       recipe = Recipe.objects.get(id=1)
       self.assertEqual(recipe.calculate_difficulty(), 'Easy')

class RecipeFormTest(TestCase):
    def test_valid_form(self):
       form = RecipeSearchForm(data={'recipe_name': 'latte', 'chart_type': '#1'})
       self.assertTrue(form.is_valid())

    def test_invalid_form(self):
       form =RecipeSearchForm()
       self.assertFalse(form.is_valid())

    def test_recipe_name(self):
       form = RecipeSearchForm()
       self.assertIn('recipe_name', form.as_p())

    def test_chart_type(self):
       form = RecipeSearchForm()
       self.assertIn('chart_type', form.as_p())
