from django.http import JsonResponse
from django.shortcuts import render,get_object_or_404
from store.models import Product
from .cart import Basket

# Create your views here.
def cart_home(request):
    return render(request,'cart/cart_home.html')

def add_to_cart_index(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        pro_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product,id=pro_id)
        basket.add_product(product=product)
        response = JsonResponse({'respone':pro_id})
        return response
