from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)

#Model for Product Category
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])

    class Meta:
        verbose_name_plural = "Categories"
    
    #to be able to better reference the data
    def __str__(self):
        return self.name

class Product(models.Model):
    #Linking the product to the category table
    category = models.ForeignKey(Category, related_name ='product', on_delete=models.CASCADE) #When the referenced object is deleted, also delete the objects that have references to it
    created_by = models.ForeignKey(User, related_name='product_creator', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    products = ProductManager()

    class Meta:
        ordering = ('-price',)

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])
    
    
    def __str__(self):
        return self.title


