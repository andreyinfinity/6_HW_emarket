from django.contrib import admin

from product.models import Version


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    """Отображение списка категорий товаров"""
    list_display = ('id', 'name',)
