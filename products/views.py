from django.shortcuts import render
from django.http import JsonResponse
from .models import Product

def product_list(request):
    products = Product.objects.all()
    data = {'products': list(products.values())}
    return JsonResponse(data)
