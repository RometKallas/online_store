from django.contrib import admin

# Register your models here.
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    #prepoluates the slug with the title
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'price',
                    'in_stock', 'created', 'updated']
    list_filter = ['in_stock', 'is_active']
    #to be able to edit directly in the admin panel
    list_editable = ['price', 'in_stock']
    #prepoluates the slug with the title
    prepopulated_fields = {'slug': ('title',)}