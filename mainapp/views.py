from django.shortcuts import render


def exchange(request):
    name = "Beka"
    
    context = {
        'name': name
    }
    return render(request, 'mainapp/index.html', context)

