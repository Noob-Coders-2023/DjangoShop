from django.shortcuts import render
from .models import Product
from django.views.generic.list import ListView


# Create your views here.

def products_view(request):
    products = Product.objects.all()

    context = {'products_list': products}
    return render(request, 'products_list.html', context)


class ProductsView(ListView):
    queryset = Product.objects.all()
    template_name = 'products_list.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(ProductsView, self).get_context_data(*args, **kwargs)
        return context