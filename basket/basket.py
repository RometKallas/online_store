from store.models import Product
from decimal import Decimal


class Basket():
    """
    A base Basket class, providing some default behavior that can be inherited or overridden
    """

    def __init__(self, request):

        #this is the key command in Django to utilize all actions with a session
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        #if the session does exist then use the same basket
        self.basket = basket

    def save(self):
        self.session.modified = True
    
    def add(self, product, qty):
        """
        Add or update the session with the basket information
        """
        product_id = product.id

        if product_id not in self.basket:
            self.basket[product_id] = {'price': str(product.price), 'qty': int(qty)}

        #we save the information into to the session
        self.save()

    #we have to make the basket iterable
    def __iter__(self):
        """
        Iterate over the products in the session data, using the product id to query and return the products from the database
        """

        #get the keys stored in the sessions basket
        product_ids = self.basket.keys()
        #get only products that are active where the id is from the keys list
        products = Product.products.filter(id__in=product_ids)
        #copy the session data
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]['product'] = product

        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item


    def __len__(self):
        """
        Get the basket data and count the qty of items
        """
        return sum(item['qty'] for item in self.basket.values()) 

    def update(self, product, qty):
        """
        Update the values in the session data
        """
        product_id = str(product)
        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty
        self.save()
    
    #loop through the basket values and add them all up
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())

    def delete(self, product):
        """
        Delete item from session data
        """
        #need to explicitly define that the product is a string because it is stored as a string in database
        product_id = str(product)
        

        if product_id in self.basket:
            del self.basket[product_id]
            #we save the information into to the session
            print(product_id)
            self.save()
        
    