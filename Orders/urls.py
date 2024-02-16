from django.urls import path

from Orders.views import add_new_order, cart

app_name = 'orders'

urlpatterns = [
    path('add-new-order', add_new_order),
    path('cart', cart)
]
