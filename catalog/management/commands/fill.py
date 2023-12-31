from django.core.management import BaseCommand, call_command
from catalog.models import Category, Product


class Command(BaseCommand):
    """Команда для первоначального заполнения БД данными из дампа БД"""
    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()
        call_command('loaddata', 'catalog_data.json')
