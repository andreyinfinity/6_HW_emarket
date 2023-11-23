import os

from django.core.management import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    """Команда для первоначального заполнения БД данными из дампа БД"""
    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()
        return os.system("python manage.py loaddata catalog_data.json")
