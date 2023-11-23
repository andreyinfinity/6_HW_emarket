from django.forms import ModelForm
from django import forms
from catalog.models import Product


class ProductForm(ModelForm):
    """Форма загрузки товаров в базу данных"""
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price', 'image']
        template_name = 'catalog/add.html'
        # Добавление классов к тегам для использования стилей CSS
        widgets = {
            'name': forms.TextInput(attrs={"class": "form field-title", "placeholder": "Название товара"}),
            'description': forms.TextInput(attrs={"class": "form field-title", "placeholder": "Описание товара"}),
            'category': forms.Select(attrs={"class": "form field-title"}),
            'price': forms.NumberInput(attrs={"class": "form field-title", "placeholder": "Стоимость товара в рублях"}),
            'image': forms.FileInput(attrs={"class": "button-light", "accept": ".jpg, .jpeg, .png, .gif"}),
        }
        # labels = {'image': 'sdf' }
