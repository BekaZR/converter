# Generated by Django 4.1.1 on 2022-10-02 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_converter_get_amount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='converter',
            options={'verbose_name': 'Конвертер валюты', 'verbose_name_plural': 'Конвертер валюты'},
        ),
    ]
