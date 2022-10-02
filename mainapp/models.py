from django.db import models

from typing import Optional, Iterable

class Converter(models.Model):
    amount = models.PositiveIntegerField(default=0, verbose_name='Сумма перевода')
    sale_currency = models.CharField(
        max_length=50, verbose_name='Продажа валюты'
    )
    buy_currency = models.CharField(
        max_length=50, verbose_name='Купля валюты'
    )
    get_amount = models.FloatField(null=True, blank=True, verbose_name='Мы получаем')
    
    def __str__(self):
        return f'{self.sale_currency} to {self.buy_currency}'
    
    
    class Meta:
        verbose_name = "Конвертер валюты"
        verbose_name_plural = "Конвертер валюты"
    