from django.shortcuts import render
from store.models import Product

# Create your views here.

def say_hello(request):
    query_set = Product.objects.filter(unit_price__range=(30, 40))
    
    return render(request, 'hello.html', {'name': '', 'products': list(query_set)}) 