from django import forms

from mainapp.models import Converter

class ConverterForm(forms.ModelForm):
    class Meta:
        model = Converter
        fields = (
            'amount', 'sale_currency', 'buy_currency', 'get_amount',
        )