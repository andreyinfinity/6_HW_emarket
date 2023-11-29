from django.db import models
from pytils.translit import slugify


class Blog(models.Model):
    """Модель для записи данных из формы обратной связи"""
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    slug = models.CharField(max_length=50, verbose_name='URL по понятиям', unique=True)
    message = models.TextField(verbose_name='текст статьи')
    preview = models.ImageField(upload_to='blog/', verbose_name='превью', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    visibility = models.BooleanField(default=True, verbose_name='признак публикации')
    viewed = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return f'{self.title}: {self.message}'

    def save(self, *args, **kwargs):
        """Переопределение save для использования slug при создании объекта"""
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(args, kwargs)

    class Meta:
        verbose_name = "Блог"
        ordering = ('-date',)
