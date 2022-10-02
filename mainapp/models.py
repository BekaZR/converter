from django.db import models


class Converter(models.Model):
    amount = models.PositiveIntegerField(default=0, verbose_name='Сумма перевода')
    sale_currency = models.CharField(
        max_length=50, verbose_name='Продажа валюты'
    )
    buy_currency = models.CharField(
        max_length=50, verbose_name='Купля валюты'
    )
    get_amount = models.PositiveIntegerField(default=0, verbose_name='Мы получаем')
    
    def __str__(self):
        return f'{self.id}'
    
    
    class Meta:
        verbose_name = "Конвертер валюты"
        verbose_name = "Конвертер валют"
        