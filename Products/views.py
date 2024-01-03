from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Product


# Create your views here.

class ProductListView(ListView):
    template_name = 'products_list.html'
    paginate_by = 1

    def get_queryset(self):
        return Product.objects.get_active_products()
