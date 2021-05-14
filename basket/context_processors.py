from .basket import Basket




#when the user sends the request to the browser the data is in the request,
def basket(request):
    #we get the data from the basket.py basket class request
    return  {'basket': Basket(request)}