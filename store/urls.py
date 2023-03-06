from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views
from pprint import pprint

# router = SimpleRouter()
# router.register('products', views.product_list)
# router.register('collections', views.collection_list)
# print(router.urls)

# URL config
urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:id>/', views.product_detail),
    path('collections/', views.collection_list),
    path('collections/<int:pk>/', views.collection_detail,
         name='collection-detail'),
]


# urlpatterns = router.urls
