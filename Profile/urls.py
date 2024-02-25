from django.urls import path

from .views import profile, profile_user_orders, profile_settings

app_name = 'profile'

urlpatterns = [
    path('profile', profile, name='profile'),
    path('profile/orders', profile_user_orders, name='orders'),
    path('profile/settings', profile_settings, name='settings'),

]
