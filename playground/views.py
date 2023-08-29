from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product

# Create your views here.

def say_hello(request):
    product = None
    try:
        product = Product.objects.get(pk=1)
    except ObjectDoesNotExist:
        pass
    if (product is not None):
        print(product.title)
    else:
        print('Product not found')
    return render(request, 'hello.html', {'name': ''}) 