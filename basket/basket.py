



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