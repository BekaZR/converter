# Generated by Django 4.1.1 on 2022-10-02 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Converter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(default=0, verbose_name='Сумма перевода')),
                ('sale_currency', models.CharField(max_length=50, verbose_name='Продажа валюты')),
                ('buy_currency', models.CharField(max_length=50, verbose_name='Купля валюты')),
                ('get_amount', models.PositiveIntegerField(default=0, verbose_name='Мы получаем')),
            ],
            options={
                'verbose_name': 'Конвертер валют',
            },
        ),
    ]
