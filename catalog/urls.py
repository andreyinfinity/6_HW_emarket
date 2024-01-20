from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog.apps import CatalogConfig
from catalog.views import CatalogView, IndexView, ContactsCreateView, \
    ProductDetailView, CategoriesView

app_name = CatalogConfig.name

urlpatterns = [
    path('', never_cache(IndexView.as_view()), name='index'),
    path('contacts/', ContactsCreateView.as_view(), name='contacts'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('product/<int:pk>/', cache_page(60 * 5)(ProductDetailView.as_view()), name='product'),
]
