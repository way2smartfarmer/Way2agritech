from django.urls import path, include

from . import views
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet, basename='products')
router.register(r'collections', views.CollectionViewSet)
router.register(r'carts', views.CartViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'orders', views.OrderViewSet, basename='orders')

products_router = routers.NestedSimpleRouter(
    router, r'products', lookup='product')
products_router.register(r'reviews', views.ReviewViewSet,
                         basename='product-reviews')
products_router.register(r'images', views.ProductImageViewSet,
                         basename='images')

carts_router = routers.NestedSimpleRouter(router, r'carts', lookup='cart')
carts_router.register(r'items', views.CartItemViewSet, basename='items')

# urlpatterns = router.urls + products_router.urls + carts_router.urls
urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(products_router.urls)),
    path(r'', include(carts_router.urls)),

]
