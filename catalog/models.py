from django.core.exceptions import ValidationError
from django.db import models

NULLABLE = {'null': True, 'blank': True}


def check_bad_words(words: str):
    """Функция проверки запрещенного слова"""
    words_list = words.split(' ')
    for word in words_list:
        if word.strip('.,?!') in ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']:
            raise ValidationError('вы используете запрещенное слово')


class Product(models.Model):
    """Модель описания товара"""
    name = models.CharField(max_length=200, verbose_name='название', validators=[check_bad_words])
    description = models.CharField(max_length=500, verbose_name='описание', validators=[check_bad_words])
    image = models.ImageField(upload_to='products/', verbose_name='изображение')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='стоимость')
    date_create = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    viewed = models.IntegerField(default=1, verbose_name='количество просмотров')
    owner = models.ForeignKey(to='users.User',  on_delete=models.SET_NULL, verbose_name='владелец', **NULLABLE)

    def __str__(self):
        return f'{self.name} ({self.description})\n{self.price}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('name',)


class Category(models.Model):
    """Модель описания категории товара"""
    name = models.CharField(max_length=200, verbose_name='название')
    description = models.CharField(max_length=500, verbose_name='описание')

    def __str__(self):
        return f'{self.name} ({self.description})'

    class Meta:
        verbose_name = 'Категория товаров'
        verbose_name_plural = 'Категории товаров'
        ordering = ('name',)


class Contacts(models.Model):
    """Модель описания контактной информации продавца"""
    name = models.CharField(max_length=200, verbose_name='название офиса')
    address = models.CharField(max_length=200, verbose_name='адрес офиса')
    phone = models.CharField(max_length=12, verbose_name='телефон')
    email = models.EmailField(verbose_name='e-mail')

    def __str__(self):
        return f'{self.name}\n{self.address}'

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'
        ordering = ('name',)


class Feedback(models.Model):
    """Модель для записи данных из формы обратной связи"""
    name = models.CharField(max_length=50, verbose_name='Имя клиента')
    phone = models.CharField(max_length=20, verbose_name='телефон')
    email = models.EmailField(verbose_name='e-mail')
    message = models.TextField(verbose_name='сообщение')
    date = models.DateTimeField(auto_now_add=True, verbose_name='дата обращения')

    def __str__(self):
        return f'{self.name}: {self.message}'

    class Meta:
        verbose_name = "Обратная связь"
        ordering = ('-date',)
