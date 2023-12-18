from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    context = {
        'message': 'Hi. Welcome to my website.'
    }
    return render(request, 'home.html', context)

def about_us(request):
    context = {
        'about': 'Hi. This is about us page.'
    }
    return render(request, 'about_us.html', context)

def contact_us(request):
    context = {
        'contact': 'Hi. This is contact us page.'
    }
    return render(request, 'contact_us.html', context)