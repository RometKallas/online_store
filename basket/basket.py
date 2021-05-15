



class Basket():
    """
    A base Basket class, providing some default behavior that can be inherited or overridden
    """

    def __init__(self, request):

        #this is the key command in Django to utilize all actions with a session
        self.session = request.session
        basket = self.session.get('skey')
        print(basket)
        print(self.session.keys())
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        #if the session does exist then use the same basket
        self.basket = basket

    def add(self, product, qty):
        """
        Add or update the session with the basket information
        """
        product_id = product.id

        if product_id not in self.basket:
            self.basket[product_id] = {'price': str(product.price), 'qty': int(qty)}

        #we save the information into to the session
        self.session.modified = True

    def __len__(self):
        """
        Get the basket data and count the qty of items
        """
        return sum(item['qty'] for item in self.basket.values()) 
