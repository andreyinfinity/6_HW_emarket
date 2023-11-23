from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, contacts, ProductView, CatalogView, ProductAdd, ProductAdded

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('product/<int:pk>', ProductView.as_view(), name='product'),
    path('add/', ProductAdd.as_view(), name='add'),
    path('added/', ProductAdded.as_view(), name='added'),
]
