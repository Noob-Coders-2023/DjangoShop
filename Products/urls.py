from django.urls import path
from django.contrib import admin
from .views import ProductListView, product_detail, SearchProducts, ProductListByCategory, product_categories_partial


app_name = 'products'

urlpatterns = [
    path('products', ProductListView.as_view(), name='products_list'),
    path('products/<product_id>/<title>', product_detail, name='product_detail'),
    path('products/search', SearchProducts.as_view()),
    path('products/<category_name>', ProductListByCategory.as_view()),
    path('admin/', admin.site.urls),
]
