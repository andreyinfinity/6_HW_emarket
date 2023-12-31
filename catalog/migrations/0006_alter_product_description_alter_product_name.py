# Generated by Django 4.2.7 on 2023-12-23 16:01

import catalog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_feedback_alter_product_category_alter_product_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=500, validators=[catalog.models.check_bad_words], verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200, validators=[catalog.models.check_bad_words], verbose_name='название'),
        ),
    ]
