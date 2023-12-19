from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm


def home(request):
    context = {
        'message': 'Hi. Welcome to my website.'
    }
    return render(request, 'home.html', context)

def about_us(request):
    context = {
        'about_us': 'Hi. This is about us page.'
    }
    return render(request, 'about_us.html', context)

def contact_us(request):
    contact_form = ContactForm()
    if request.method == "POST":
        print(request.POST.get('fullname'))
        print(request.POST.get('email'))
        print(request.POST.get('message'))
    context = {
        'contact_us': 'Hi. This is contact us page.',
        'contact_form': contact_form
    }
    return render(request, 'contact_us.html', context)