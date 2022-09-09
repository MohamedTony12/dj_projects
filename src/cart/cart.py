class Basket:
    def __init__(self, request) -> None:
        self.session = request.session
        cart = self.session.get('skey')
        if 'skey' not in request.session:
            cart = self.session['skey'] = {}
        self.cart = cart

    def add_product(self, product, qty=1):
        prod_id = str(product.id)
        if prod_id not in self.cart:
            self.cart[prod_id] = {'price': str(
                product.selling_price), 'qty': int(qty)}
        else:
            self.cart[prod_id]['qty'] =  int(qty) + 1
        self.session.modified = True
