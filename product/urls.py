from django.urls import path
from product.apps import ProductConfig
from product.views import ProductCreate, ProductList, ProductUpdate, ProductDelete, VersionCreate, VersionList, \
    VersionUpdate, VersionDelete

app_name = ProductConfig.name


urlpatterns = [
    path('management/product/create/', ProductCreate.as_view(), name='create'),
    path('management/product/', ProductList.as_view(), name='list'),
    path('management/product/<int:pk>/update/', ProductUpdate.as_view(), name='update'),
    path('management/product/<int:pk>/delete/', ProductDelete.as_view(), name='delete'),
    path('management/version/create/', VersionCreate.as_view(), name='create_ver'),
    path('management/version/', VersionList.as_view(), name='list_ver'),
    path('management/version/<int:pk>/update/', VersionUpdate.as_view(), name='update_ver'),
    path('management/version/<int:pk>/delete/', VersionDelete.as_view(), name='delete_ver'),
]
