from django.contrib import admin
from django.forms import inlineformset_factory
# from .models import Product, ProductImage
from .models import Product, ProductGallery


# Register your models here.


# class ProductImageInline(admin.TabularInline):
#     model = ProductImage
#     extra = 1  # Number of empty forms to display


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'price', 'active', 'featured']
    # inlines = [ProductImageInline]


class Meta:
    model = Product


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductGallery)
