from rest_framework import serializers

from store.models import Product, Collection


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']


products_count = serializers.IntegerField()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'slug', 'inventory',
                  'price', 'collection', 'description',]

    price = serializers.DecimalField(
        max_digits=6, decimal_places=2, source='unit_price')

    # collection = serializers.HyperlinkedRelatedField(
    #     queryset=Collection.objects.all(),
    #     view_name='collection-detail'
    # )


# def create(self,validated_data):
#     product=Product(**validated_data)
#     product.other=1
#     product.save()
#     return product

# def update(self,instance,validated_data):
#     instance.unit_price =validated_data.get('unit_price')
#     instance.save()
#     return instance
