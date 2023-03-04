from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product

# # Create your views here.


def say_hello(request):
    # queryset = Product.objects.get(pk=1)

    return render(request, 'hello.html,', {'name': 'AgriTech'})
