from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import products_view, ProductsView

app_name = "products"

urlpatterns = [
    path('products-fb', products_view),
    path('products-cb', ProductsView.as_view()),
]
