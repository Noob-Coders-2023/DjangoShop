from django.urls import path
from .views import ProductListView, product_detail, SearchProducts


app_name = 'products'

urlpatterns = [
    path('products', ProductListView.as_view(), name='products_list'),
    path('products/<product_id>/<title>', product_detail, name='product_detail'),
    path('products/search', SearchProducts.as_view())
]
