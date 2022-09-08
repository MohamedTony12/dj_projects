
from django.urls import path
from . import views

app_name='store'

urlpatterns = [
    path('',views.store_home,name='store_home'),
    path('product/category/<slug:cat_id>',views.store_category,name='store_category'),
    path('product/detail/<slug:pro_slug>',views.product_detail,name='product_detail'),
]
