from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm, LoginForm, RegisterForm


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
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            print('Error')


    context = {
        'title': 'Login Page',
        'message': 'Login Form',
        'login_form': login_form
    }
    return render(request, 'auth/login.html', context)

User = get_user_model()
def register_page(request):
    register_form = RegisterForm(request.POST or None)

    if register_form.is_valid():
        username = register_form.cleaned_data.get('username')
        email = register_form.cleaned_data.get('email')
        password = register_form.cleaned_data.get('password')
        User.object.create_user(username=username, email=email, password=password)

    context = {
        'title': 'Register Page',
        'message': 'Register Form',
        'register_form': register_form
    }
    return render(request, 'auth/register.html', context)
