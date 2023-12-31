# Generated by Django 4.2.7 on 2023-11-29 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='message',
            field=models.TextField(verbose_name='текст статьи'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.CharField(max_length=50, unique=True, verbose_name='URL по понятиям'),
        ),
    ]
