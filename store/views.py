from django.shortcuts import render

from .models import Category, Product
# Create your views here.

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def homepage(request):
    #Running a query against the product table to collect all data
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})
