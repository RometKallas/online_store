from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .basket import Basket

# Create your views here.
def basket_summary(request):
    return render(request, 'store/basket/basket_summary.html')

#we need to get the data that the ajax request is collecting from the productid
def basket_add(request):
    #get the session data
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product)
