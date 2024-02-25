from django.shortcuts import render


# Create your views here.

def profile(request):
    context = {}
    return render(request, 'profile.html', context)


def profile_user_orders(request):
    context = {}
    return render(request, 'profile_user_orders.html', context)


def profile_settings(request):
    context = {}
    return render(request, 'profile_settings.html', context)


def profile_sidebar(request):
    context = {}
    return render(request, 'profile_sidebar.html', context)
