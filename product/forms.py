from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Product
from product.models import Version


class StyleFormMixin:
    """Миксин для применения стилей к полям формы"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.input_type == 'text':
                field.widget.attrs['class'] = 'form field-title'
                field.widget.attrs['placeholder'] = field.label
            elif field.widget.input_type == 'select':
                field.widget.attrs['class'] = 'form field-title'
            elif field.widget.input_type == 'number':
                field.widget.attrs['class'] = 'form field-title'
            elif field.widget.input_type == 'file':
                field.widget.attrs['class'] = 'button-light'
                field.widget.attrs['accept'] = '.jpg, .jpeg, .png, .gif'


def check_bad_words(word: str) -> bool:
    """Функция проверки запрещенного слова"""
    if word in ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']:
        return True
    return False


class ProductForm(StyleFormMixin, forms.ModelForm):
    """Форма для создания и редактирования продукта"""
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price', 'image']

    def clean_name(self):
        """Метод валидации поля name на запрещенные слова"""
        cleaned_data = self.cleaned_data.get('name')
        if check_bad_words(cleaned_data):
            raise ValidationError('Это слово запрещено использовать')
        return cleaned_data

    def clean_description(self):
        """Метод валидации поля description на запрещенные слова"""
        cleaned_data = self.cleaned_data.get('description')
        if check_bad_words(cleaned_data):
            raise ValidationError('Это слово запрещено использовать')
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    """Форма для создания и редактирования версии продукта"""
    class Meta:
        model = Version
        fields = '__all__'

    def clean(self):
        """Проверка на уникальность пары полей num и product_pk.
        Для конкретного продукта номера версий должны различаться"""
        cleaned_data = self.cleaned_data
        num = cleaned_data.get('num')
        prod_pk = cleaned_data.get('product').pk
        # Проверяем менялось ли поле num, если нет, пропускаем проверку
        if 'num' in self.changed_data:
            # Если значение num для продукта уже есть в БД, вызываем исключение
            if Version.objects.filter(product=prod_pk, num=num).exists():
                raise ValidationError("Такая версия продукта уже есть")
