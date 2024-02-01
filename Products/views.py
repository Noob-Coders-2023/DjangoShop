from django.http import Http404
from django.shortcuts import render
from django.views.generic.list import ListView

from Category.models import Category
from Tags.models import Tag
from .models import Product, ProductGallery


# Create your views here.

class ProductListView(ListView):
    template_name = 'products_list.html'
    paginate_by = 5

    def get_queryset(self):
        return Product.objects.get_active_products()


class ProductCategoru:
    pass


class ProductListByCategory(ListView):
    template_name = 'products_list.html'
    paginate_by = 5

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        categories = Category.objects.filter(name__iexact=category_name)
        if categories is None:
            raise Http404('صفحه مورد نظر یافت نشد.')

        return Product.objects.get_products_by_category(category_name)


def product_categories_partial(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'categories_view_partial.html', context)


def product_detail(request, *args, **kwargs):
    get_product_id = kwargs['product_id']
    title = kwargs['title']

    product = Product.objects.get_product_by_id(get_product_id)
    if product is None:
        raise Http404('محصول موردنظر یافت نشد.')

    gallery = ProductGallery.objects.filter(product_id=get_product_id)

    context = {
        'product': product,
        'gallery': gallery
    }

    tag = Tag.objects.first()
    # print(tag)
    # print(tag.products.all())
    # print(product.tag_set.all())

    return render(request, 'products_detail.html', context)


class SearchProducts(ListView):
    template_name = 'products_list.html'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query is not None:
            return Product.objects.search_products(query)

        return Product.objects.get_active_products()
