from django.urls import path
from product.apps import ProductConfig
from product.views import ProductCreate, ProductList, ProductUpdate, ProductDelete, VersionCreate, VersionList, \
    VersionUpdate, VersionDelete

app_name = ProductConfig.name


urlpatterns = [
    path('product/create/', ProductCreate.as_view(), name='create'),
    path('product/', ProductList.as_view(), name='list'),
    path('product/<int:pk>/update/', ProductUpdate.as_view(), name='update'),
    path('product/<int:pk>/delete/', ProductDelete.as_view(), name='delete'),
    path('version/create/', VersionCreate.as_view(), name='create_ver'),
    path('version/', VersionList.as_view(), name='list_ver'),
    path('version/<int:pk>/update/', VersionUpdate.as_view(), name='update_ver'),
    path('version/<int:pk>/delete/', VersionDelete.as_view(), name='delete_ver'),
]
