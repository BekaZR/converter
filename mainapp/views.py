import requests

from django.shortcuts import render

from mainapp.forms import ConverterForm


def index(request):
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    response = requests.get(url).json()
    currencies = response.get('rates')
    
    if request.method == 'POST':
        form = ConverterForm(request.POST)
    else:
        form = ConverterForm()
    context = {
        'form': form,
        'currencies': currencies,
    }
    return render(request, 'mainapp/index.html', context)

