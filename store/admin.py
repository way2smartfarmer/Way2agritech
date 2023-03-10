from django.contrib import admin, messages
from . import models
from django.db.models.query import QuerySet
from django.db.models import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse
from .models import ProductImage


class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inventory'

    def lookups(self, request, model_admin):
        return [
            ('<10', 'Low')
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<10':
            return queryset.filter(inventory__lt=10)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    readonly_fields = ['thumbnail']

    def thumbnail(self, instance):
        if instance.image.name != '':
            return format_html(f'<img src="{instance.image.url}" class="thumbnail"/>')
        return ''


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):

    autocomplete_fields = ['collection']
    search_fields = ['title']
    prepopulated_fields = {
        'slug': ['title']
    }
    # exclude = ['promotions']

    actions = ['clear_inventory']
    inlines = [ProductImageInline]
    list_display = ['title', 'unit_price',
                    'inventory', 'collection']
    list_editable = ['unit_price']
    list_filter = ['collection', 'last_update', InventoryFilter]
    list_per_page = 10
    list_select_related = ['collection']


def collection_title(self, product):
    return product.collection.title


@admin.display(ordering='inventory')
def inventory_status(self, product):
    if product.inventory < 10:
        return 'Low'
    return 'Ok'


@admin.action(description='Clear Inventory')
def clear_inventory(self, request, queryset):
    updated_count = queryset.update(inventory=0)
    self.message_user(
        request,
        f'{updated_count} products were succesfully updated.',
        messages.ERROR
    )


class Media:
    css = {
        'all': ['store/styles.css']
    }


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    autocomplete_fields = ['featured_product']
    list_display = ['title', 'products_count']
    search_fields = ['title_istartswith']

    @admin.display(ordering='products_count')
    def products_count(self, collection):
        url = (reverse('admin:store_product_changelist')
               + '?'
               + urlencode({
                   'collection_id': str(collection.id)
               }))
        return format_html('<a href="{}">{} Products</a>', url,
                           collection.products_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('products')
        )


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership', 'orders']
    list_editable = ['membership']
    list_per_page = 10
    list_select_related = ['user']
    ordering = ['user__first_name', 'user__last_name']
    search_fields = ['first_name__istartswith', 'last_name__startswith']

    @admin.display(ordering='orders_count')
    def orders(self, customer):
        url = (
            reverse('admin:store_order_changelist')
            + '?'
            + urlencode({
                'customer__id': str(customer.id)
            }))
        return format_html('<a href="{}">{} Orders</a>', url, customer.orders_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            orders_count=Count('order')
        )


class OrderItemInline(admin.TabularInline):
    autocomplete_fields = ['product']
    model = models.OrderItem
    min_num = 1
    max_num = 10
    extra = 0


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customer']
    inlines = [OrderItemInline]
    list_display = ['id', 'placed_at', 'customer']


# admin.site.register(models.Collection)
