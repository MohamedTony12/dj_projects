

from multiprocessing import context
from django.shortcuts import render,get_object_or_404
from .models import Category,Product


def store_home(request):
    product = Product.objects.all().order_by('?')
    context = {
    'product':product
    }
    return render(request,'store/index.html',context)


def store_category(request,cat_id):
    category = get_object_or_404(Category,slug=cat_id)
    product = Product.objects.filter(category=category)
    context = {
        'cat_pro':product
    }   
    return render(request,'store/product_category.html',context)


def product_detail(request,pro_slug):
    product = get_object_or_404(Product,slug=pro_slug)
    context = {
        'product':product
    }   
    return render(request,'store/product_detail.html',context)
