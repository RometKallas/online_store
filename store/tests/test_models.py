from django.test import TestCase

from django.contrib.auth.models import User
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

    def test_category_model_entry(self):
        """
        Test Category model return name
        """
        data = self.data1
        self.assertEqual(str(data), 'sqchair')


class TestProductsModel(TestCase):
    def setUp(self):
        Category.objects.create(name='sqchair', slug='sqchair')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title='Children Chair', created_by_id=1,
                                            slug='children-chair', price='59.00', image='randomimage')
    
    def test_products_model_entry(self):
        """
        Test product model data insertion/types/field attributes
        """
        data = self.data1
        #is instance as expected
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'Children Chair')