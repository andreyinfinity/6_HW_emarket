# Generated by Django 4.2.7 on 2023-11-17 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_contacts_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='viewed',
            field=models.IntegerField(default=1, verbose_name='количество просмотров'),
        ),
    ]