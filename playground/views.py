from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from django.db.models import Q, F
# from django.db.models.aggregates import Count,Max,Min,Avg,Sum


# # Create your views here.


def say_hello(request):
    # queryset = Product.objects.get(pk=1)

    # for product in queryset:
    #     print(product)

    #   queryset = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price_lt=20))
    #   queryset = Product.objects.filter(inventory=F('unit_price'))
    #   queryset = Product.objects.values('id,'title','collection__title')
    return render(request, 'hello.html,', {'name': 'AgriTech'})
    # return HttpResponse('hello')
