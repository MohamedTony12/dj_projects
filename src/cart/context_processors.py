from urllib import request
from .cart import Basket

def cart(request):
    context = {
        'cart':Basket(request)
    }
    return context
