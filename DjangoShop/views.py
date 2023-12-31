from django.shortcuts import render


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