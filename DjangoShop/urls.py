"""
URL configuration for DjangoShop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from DjangoShop import settings
from .views import home, header, footer, contact_us, login_page, register_page, logout_page
from Products.views import ProductListView, product_categories_partial

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('header', header, name='header'),
    path('footer', footer, name='footer'),
    path('contact-us', contact_us, name='contact'),
    path('login', login_page, name='login'),
    path('register', register_page, name='register'),
    path('logout', logout_page, name='logout'),
    path('', include('Products.urls', namespace='products')),
    path('product_categories_partial', product_categories_partial, name='product_categories_partial')
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
