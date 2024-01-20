from django.urls import path
from django.views.decorators.cache import never_cache

from product.apps import ProductConfig
from product.views import ProductCreate, ProductList, ProductUpdate, ProductDelete, VersionCreate, VersionList, \
    VersionUpdate, VersionDelete

app_name = ProductConfig.name


urlpatterns = [
    path('product/create/', never_cache(ProductCreate.as_view()), name='create'),
    path('product/', never_cache(ProductList.as_view()), name='list'),
    path('product/<int:pk>/update/', never_cache(ProductUpdate.as_view()), name='update'),
    path('product/<int:pk>/delete/', never_cache(ProductDelete.as_view()), name='delete'),
    path('version/create/', VersionCreate.as_view(), name='create_ver'),
    path('version/', VersionList.as_view(), name='list_ver'),
    path('version/<int:pk>/update/', VersionUpdate.as_view(), name='update_ver'),
    path('version/<int:pk>/delete/', VersionDelete.as_view(), name='delete_ver'),
]
