from django.core.cache import cache
from catalog.models import Category
from config import settings


def get_categories():
    """Получение списка категорий с низкоуровневым кешированием"""
    if settings.CACHE_ENABLED:
        categories = cache.get('categories')
        if categories is None:
            categories = Category.objects.all()
            cache.set('categories', categories)
    else:
        categories = Category.objects.all()
    return categories
