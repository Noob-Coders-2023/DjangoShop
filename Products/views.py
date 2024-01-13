from django.http import Http404
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Product


# Create your views here.

class ProductListView(ListView):
    template_name = 'products_list.html'
    paginate_by = 2

    def get_queryset(self):
        return Product.objects.get_active_products()


def product_detail(request, *args, **kwargs):
    product_id = kwargs['product_id']
    title = kwargs['title']

    product = Product.objects.get_product_by_id(product_id)
    if product is None:
        raise Http404('محصول موردنظر یافت نشد.')

    context = {
        'product': product
    }
    return render(request, 'products_detail.html', context)


class SearchProducts(ListView):
    template_name = 'products_list.html'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query is not None:
            return Product.objects.search_products(query)

        return Product.objects.get_active_products()
