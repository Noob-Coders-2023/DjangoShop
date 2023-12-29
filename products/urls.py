from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import products_view, ProductsView, product_detail, ProductDetailView, ProductActiveList, ProductActiveDetail

app_name = "products"

urlpatterns = [
    path('products-fb', products_view),
    path('products-cb', ProductsView.as_view()),
    path('products-fb/<productID>', product_detail),
    path('products-cb/<pk>', ProductDetailView.as_view()),
    path('products-active', ProductActiveList.as_view()),
    path('products-active/<pk>', ProductActiveDetail.as_view()),
]
