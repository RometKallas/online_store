from django.shortcuts import render, get_object_or_404
#get object is a shortcut to access data from the database
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

def product_detail(request, slug):
    #based on the slug it is gettign the product we need to return
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/product_page.html', {'product': product})
