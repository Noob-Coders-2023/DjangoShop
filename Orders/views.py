from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from Orders.forms import UserNewOrderForm
from Orders.models import Order
from Products.models import Product


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
