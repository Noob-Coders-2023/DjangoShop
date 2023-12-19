from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm, LoginForm


def home(request):
    print(request.user.is_authenticated)
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


def login_page(request):
    print(request.user.is_authenticated)
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        username = login_form.cleaned_data.get('username')
        print(username)
        password = login_form.cleaned_data.get('password')
        print(password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            print('Error')


    context = {
        'message': 'Hi. This is login page.',
        'login_form': login_form
    }
    return render(request, 'auth/login.html', context)


def register_page(request):
    pass
