from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Product
# from django.views.generic import ListView, DetailView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


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


def product_detail(request, productID):
    # product = Product.objects.get(id=productID)
    product = get_object_or_404(Product, id=productID)

    context = {
        "product": product
    }
    return render(request, 'product_detail.html', context)


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'product_detail.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        return context

    def get_object(self, *args, **kwargs):
        productId = self.kwargs.get('pk')
        product = Product.objects.get_product_by_id(productId)
        if product is None:
            raise Http404("Product not found.")
        return product


class ProductActiveList(ListView):
    template_name = "products_list.html"

    def get_queryset(self):
        return Product.objects.get_active_products()


class ProductActiveDetail(DetailView):
    template_name = "product_detail.html"

    def get_queryset(self):
        return Product.objects.get_active_products()
