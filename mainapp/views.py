from django.shortcuts import render

from mainapp.forms import ConverterForm


def index(request):
    if request.method == 'POST':
        form = ConverterForm(request.POST)
    else:
        form = ConverterForm()
    context = {
        'form': form
    }
    return render(request, 'mainapp/index.html', context)

