from django.test import TestCase

from store.models import Category, Product
# Create your tests here.

class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='sqchair', slug='sqchair')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        #If the "data" fits the Category model then the isinstance will return True
        self.assertTrue(isinstance(data, Category))