from django.urls import path

from Orders.views import add_new_order

app_name = 'orders'

urlpatterns = [
    path('add-new-order', add_new_order)
]
