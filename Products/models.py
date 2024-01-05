import random
from django.db import models
import os


# Create your models here.
def get_file_extension(file):
    base_name = os.path.basename(file)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image(instance, filename):
    rand_name = random.randint(1, 999999999)
    name, ext = get_file_extension(filename)
    final_name = f"{instance.id}-{rand_name}{ext}"
    return f"products/{filename}"


class ProductManager(models.Manager):
    def get_active_products(self):
        return self.get_queryset().filter(active=True)

    def get_product_by_id(self, product_id):
        qs = self.get_queryset().filter(id=product_id, active=True)
        if qs.count() == 1:
            return qs.first()
        else:
            return None


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان محصول')
    description = models.TextField(verbose_name='توضیحات')
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='قیمت')
    image = models.ImageField(upload_to=upload_image, null=True, blank=True, verbose_name='تصویر')
    active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')
    time = models.DateTimeField(auto_now_add=True, )

    objects = ProductManager()

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.title

    def get_product_detail_url(self) :
        return f"/products/{self.id}/{self.title.replace(' ', '-')}"
