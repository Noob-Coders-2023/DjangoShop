from django.urls import path
from .views import ProductListView, product_detail


app_name = 'products'

urlpatterns = [
    path('products', ProductListView.as_view(), name='products_list'),
    path('product-detail/<product_id>/<title>', product_detail, name='product_detail'),
]
