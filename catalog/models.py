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

    def __str__(self):
        return f'{self.name} ({self.description})\n{self.price}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('name',)


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='название')
    description = models.CharField(max_length=500, verbose_name='описание')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Название категории: {self.name} ({self.description})'

    class Meta:
        verbose_name = 'Категория товаров'
        verbose_name_plural = 'Категории товаров'
        ordering = ('name',)
