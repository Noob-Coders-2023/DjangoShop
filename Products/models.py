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


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان محصول')
    description = models.TextField(verbose_name='توضیحات')
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='قیمت')
    image = models.ImageField(upload_to=upload_image, null=True, blank=True, verbose_name='تصویر')
    active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')
    time = models.DateTimeField(auto_now_add=True,)

    def __str__(self):
        return self.title