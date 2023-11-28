from django import forms
from catalog.models import Product, Feedback


class ProductForm(forms.ModelForm):
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


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'phone', 'email', 'message']
        template_name = 'catalog/contacts.html'
        # Добавление классов к тегам для использования стилей CSS
        widgets = {
            'name': forms.TextInput(attrs={"class": "form field-title", "placeholder": "Имя"}),
            'phone': forms.TextInput(attrs={"class": "form field-title", "placeholder": "+7-999-99-99-99"}),
            'email': forms.EmailInput(attrs={"class": "form field-title", "placeholder": "e@mail.ru"}),
            'message': forms.TextInput(attrs={"class": "form field-title", "placeholder": "Введите ваш вопрос"}),
        }
