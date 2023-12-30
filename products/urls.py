from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import (products_view, ProductsView,
                    product_detail, ProductDetailView,
                    ProductsActiveList, ProductsActiveDetail,
                    ProductShowWithSlug)

app_name = "products"

urlpatterns = [
    path('', products_view, name='productView'),
    path('<slug>', ProductShowWithSlug.as_view(), name='detail'),
    # path('products-cb', ProductsView.as_view()),
    # path('products-fb/<productID>', product_detail),
    # path('products-cb/<pk>', ProductDetailView.as_view()),
    # path('products-active', ProductsActiveList.as_view()),
    # path('products-active/<pk>', ProductsActiveDetail.as_view()),
]
