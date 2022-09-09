
from django.urls import path
from . import views

app_name='cart'

urlpatterns = [
    path('cart',views.cart_home,name='cart_home'),
    path('add-to-cart',views.add_to_cart_index,name='addtocartindex'),
]
