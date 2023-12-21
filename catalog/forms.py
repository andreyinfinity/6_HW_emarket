from django import forms
from catalog.models import Feedback


class FeedbackForm(forms.ModelForm):
    """Форма получения обратной связи от посетителя"""
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
