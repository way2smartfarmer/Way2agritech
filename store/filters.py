from django_filters.rest_framework import FilterSet
from .models import Product
from django_filters import rest_framework as filters


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'collection_id': ['exact'],
            'unit_price': ['gt', 'lt']
        }


class SubCollectionFilter(filters.FilterSet):
    subcollection = filters.CharFilter(
        field_name='collection__subcollection__title', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['collection', 'subcollection', 'unit_price']
