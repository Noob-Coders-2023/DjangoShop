from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from Orders.forms import UserNewOrderForm
from Orders.models import Order, OrderDetail
from Products.models import Product

# ZarinPal
from django.conf import settings
import requests
import json


# Create your views here.

@login_required(login_url='/login')
def add_new_order(request):
    new_order_form = UserNewOrderForm(request.POST or None)
    if new_order_form.is_valid():
        order = Order.objects.filter(user_id=request.user.id, paid=False).first()
        if order is None:
            order = Order.objects.create(user_id=request.user.id, paid=False)

        product_id = new_order_form.cleaned_data.get('product_id')
        product = Product.objects.get_product_by_id(product_id)
        count = new_order_form.cleaned_data.get('count')
        if count < 0:
            count = 1
        order.orderdetail_set.create(product_id=product.id, count=count, price=product.price)
        return redirect(f'/products/{product.id}/{product.title.replace(" ", "-")}')


def cart(request):
    context = {
        'order': None,
        'details': None,
        'total_price': 0,
    }

    open_order: Order = Order.objects.filter(user_id=request.user.id, paid=False).first()
    if open_order is not None:
        context['order'] = open_order
        context['details'] = open_order.orderdetail_set.all()
        context['total_price'] = open_order.get_total_price()

    return render(request, 'cart.html', context)


@login_required(login_url='/login')
def remove_order(request, *args, **kwargs):
    detail_id = kwargs['detail_id']
    order_detail = OrderDetail.objects.get_queryset().get(id=detail_id, order__user_id=request.user.id)
    if order_detail is not None:
        order_detail.delete()
        return redirect('/cart')
    raise Http404()


# Zarinpal Codes

# # ? sandbox merchant
# if settings.SANDBOX:
#     sandbox = 'sandbox'
# else:
#     sandbox = 'www'
#
# ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
# ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
# ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"
#
# amount = 1000  # Rial / Required
# description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
# phone = 'YOUR_PHONE_NUMBER'  # Optional
# # Important: need to edit for realy server.
# CallbackURL = 'http://127.0.0.1:8080/verify/'
# #
# #
# def send_request(request):
#     open_order: Order = Order.objects.filter(user_id=request.user.id, paid=False).first()
#     if open_order is not None:
#         total_price = open_order.get_total_price()
#         data = {
#             "MerchantID": settings.MERCHANT,
#             "Amount": total_price,
#             "Description": description,
#             "Phone": phone,
#             "CallbackURL": CallbackURL,
#         }
#         data = json.dumps(data)
#         # set content length by data
#         headers = {'content-type': 'application/json', 'content-length': str(len(data))}
#         try:
#             response = requests.post(ZP_API_REQUEST, data=data, headers=headers, timeout=10)
#
#             if response.status_code == 200:
#                 response = response.json()
#                 if response['Status'] == 100:
#                     return {'status': True, 'url': ZP_API_STARTPAY + str(response['Authority']),
#                             'authority': response['Authority']}
#                 else:
#                     return {'status': False, 'code': str(response['Status'])}
#             return response
#
#         except requests.exceptions.Timeout:
#             return {'status': False, 'code': 'timeout'}
#         except requests.exceptions.ConnectionError:
#             return {'status': False, 'code': 'connection error'}
#
#
# def verify(authority):
#     data = {
#         "MerchantID": settings.MERCHANT,
#         "Amount": amount,
#         "Authority": authority,
#     }
#     data = json.dumps(data)
#     # set content length by data
#     headers = {'content-type': 'application/json', 'content-length': str(len(data))}
#     response = requests.post(ZP_API_VERIFY, data=data, headers=headers)
#
#     if response.status_code == 200:
#         response = response.json()
#         if response['Status'] == 100:
#             return {'status': True, 'RefID': response['RefID']}
#         else:
#             return {'status': False, 'code': str(response['Status'])}
#     return response
