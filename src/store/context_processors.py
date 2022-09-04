from multiprocessing import context
from .models import Category


def category(request):
    context = {
        'category':Category.objects.all()}
    return context
        
    

