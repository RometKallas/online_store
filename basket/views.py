from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from store.models import Product
from .basket import Basket

# Create your views here.
def basket_summary(request):
    basket = Basket(request)
    return render(request, 'store/basket/basket_summary.html', {'basket': basket})

#we need to get the data that the ajax request is collecting from the productid
def basket_add(request):
    #get the session data
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)
        
        basketqty = basket.__len__()
        response = JsonResponse({'qty':basketqty})
        
        return response

def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        basket.delete(product=product_id)

