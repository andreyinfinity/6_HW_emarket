from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='название')
    description = models.CharField(max_length=500, verbose_name='описание')
    image = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price = models.IntegerField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    viewed = models.IntegerField(default=1, verbose_name='количество просмотров')

    def __str__(self):
        return f'{self.name} ({self.description})\n{self.price}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('name',)


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='название')
    description = models.CharField(max_length=500, verbose_name='описание')

    def __str__(self):
        return f'{self.name} ({self.description})'

    class Meta:
        verbose_name = 'Категория товаров'
        verbose_name_plural = 'Категории товаров'
        ordering = ('name',)


class Contacts(models.Model):
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
