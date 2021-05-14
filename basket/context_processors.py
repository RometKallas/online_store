from .basket import Basket



#context processor can be used site wide
#we use the context processor so that this is running every time a template is loaded
#when the user sends the request to the browser the data is in the request,
def basket(request):
    #we get the data from the basket.py basket class request
    return  {'basket': Basket(request)}