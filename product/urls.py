from django.urls import path
from product.apps import ProductConfig
from product.views import ProductCreate, ProductList, ProductUpdate, ProductDelete

app_name = ProductConfig.name


urlpatterns = [
    path('management/product/create/', ProductCreate.as_view(), name='create'),
    path('management/product/', ProductList.as_view(), name='list'),
    path('management/product/<int:pk>/update/', ProductUpdate.as_view(), name='update'),
    path('management/product/<int:pk>/delete/', ProductDelete.as_view(), name='delete'),
]
