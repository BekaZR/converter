import requests

from django.shortcuts import render

from mainapp.forms import ConverterForm


def index(request):
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    response = requests.get(url).json()
    currencies = response.get('rates')
    
    if request.method == 'GET':
        context = {
        'currencies': currencies,
    }
        return render(request, 'mainapp/index.html', context)
    
    if request.method == 'POST':
        form = ConverterForm(request.POST)
        form.is_valid()
        amount = form.cleaned_data.get('amount')
        sale_currency = form.cleaned_data.get('sale_currency')
        buy_currency = form.cleaned_data.get('buy_currency')
        
        
        converted_amount = round(
            (
                currencies.get(buy_currency) / currencies.get(sale_currency)
                    ) * float(amount), 2
            )
        
        
    else:
        form = ConverterForm()
    
    context = {
        'form': form,
        'currencies': currencies,
        'converted_amount': converted_amount,
    }
    return render(request, 'mainapp/index.html', context)
