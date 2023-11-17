# Generated by Django 4.2.7 on 2023-11-17 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='название офиса')),
                ('address', models.CharField(max_length=200, verbose_name='адрес офиса')),
                ('phone', models.IntegerField(max_length=11, verbose_name='телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail')),
            ],
            options={
                'verbose_name': 'Контакты',
                'verbose_name_plural': 'Контакты',
                'ordering': ('name',),
            },
        ),
    ]