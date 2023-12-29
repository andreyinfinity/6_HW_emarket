from django.db import models
from django.db.models import Q


class Version(models.Model):
    """Модель версии товара"""
    name = models.CharField(max_length=200, verbose_name='название')
    num = models.IntegerField(verbose_name='номер')
    is_active = models.BooleanField(default=False, verbose_name='активная?')
    product = models.ForeignKey('catalog.Product', on_delete=models.CASCADE, verbose_name='продукт')

    def __str__(self):
        return f'{self.name} {self.num}'

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['product'],
                condition=Q(is_active=True),
                name='only_one_active_version_for_product'
            ),
            models.UniqueConstraint(
                fields=['num', 'product'],
                name='unique_together_version_num_and_product'
            )]
        # unique_together = [['num', 'product']]
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
        ordering = ('-num',)
