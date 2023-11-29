from django.contrib import admin

from catalog.models import Category, Product, Contacts


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Отображение списка категорий товаров"""
    list_display = ('id', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Отображение списка товаров с фильтрацией по категориям и поиск"""
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    """Отображение контактов компании с поиском по имени"""
    list_display = ('id', 'name', 'address', 'phone', 'email')
    search_fields = ('name',)
