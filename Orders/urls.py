from django.urls import path

from Orders.views import add_new_order, cart
# , send_request, verify)

app_name = 'orders'

urlpatterns = [
    path('add-new-order', add_new_order),
    path('cart', cart),
    # path('request/', send_request, name='request'),
    # path('verify/<order_id>', verify, name='verify'),
]
