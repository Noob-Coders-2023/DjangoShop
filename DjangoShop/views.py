from django.contrib.auth import authenticate, login, get_user_model, logout
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from Sliders.models import Slider
from Settings.models import Settings
from Products.models import Product


def header(request):
    setting = Settings.objects.first()
    context = {
        'menu_item': 'منوی سفارشی از رندر پارشیال',
        'setting': setting
    }
    return render(request, 'base/header.html', context)


def footer(request):
    setting = Settings.objects.first()
    context = {
        'setting': setting
    }
    return render(request, 'base/footer.html', context)


def home(request):
    featured_products = Product.objects.filter(featured=True)
    most_viewed_products = Product.objects.order_by('-visits').all()[:5]
    latest_products = Product.objects.order_by('-id').all()[:5]
    sliders = Slider.objects.filter(active=True)
    context = {
        'sliders': sliders,
        'featured_products': featured_products,
        'most_viewed_products': most_viewed_products,
        'latest_products': latest_products,
    }
    return render(request, 'home.html', context)


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
