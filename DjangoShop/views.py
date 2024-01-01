from django.contrib.auth import authenticate, login, get_user_model, logout
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm


def header(request):
    context = {
        'menu_item': 'منوی سفارشی از رندر پارشیال'
    }
    return render(request, 'base/header.html', context)


def footer(request):
    context = {}
    return render(request, 'base/footer.html', context)


def home(request):
    context = {}
    return render(request, 'home.html', context)


def contact_us(request):
    context = {}
    return render(request, 'contact_us.html', context)


# AUTH section

def login_page(request):
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
        'login_form': login_form
    }
    return render(request, 'login.html', context)


User = get_user_model()


def register_page(request):
    register_form = RegisterForm(request.POST or None)
    if register_form.is_valid():
        username = register_form.cleaned_data.get('username')
        email = register_form.cleaned_data.get('email')
        password = register_form.cleaned_data.get('password')
        new_user = User.objects.create_user(username=username, email=email, password=password)

    context = {
        'register_form': register_form
    }
    return render(request, 'register.html', context)


def logout_page(request):
    logout(request)
    return redirect('/login')
