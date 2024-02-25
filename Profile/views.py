from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render

from Orders.models import Order
from .forms import UserEditProfileForm


# Create your views here.
@login_required(login_url='/login')
def profile(request):
    context = {}
    return render(request, 'profile.html', context)


@login_required(login_url='/login')
def profile_user_orders(request):
    user_id = request.user.id
    orders = Order.objects.get(user_id=user_id)
    context = {}
    return render(request, 'profile_user_orders.html', context)


@login_required(login_url='/login')
def profile_settings(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    if user is None:
        raise Http404()

    edit_profile = UserEditProfileForm(request.POST or None,
                                       initial={'first_name': user.first_name,
                                                'last_name': user.last_name,
                                                'email': user.email})
    if edit_profile.is_valid():
        first_name = edit_profile.cleaned_data.get('first_name')
        last_name = edit_profile.cleaned_data.get('last_name')
        email = edit_profile.cleaned_data.get('email')

        user.first_name = first_name
        user.last_name = last_name
        user.email = email

        user.save()

    context = {
        'edit_profile': edit_profile
    }
    return render(request, 'profile_settings.html', context)


@login_required(login_url='/login')
def profile_sidebar(request):
    context = {}
    return render(request, 'profile_sidebar.html', context)
