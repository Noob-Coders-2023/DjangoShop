import random
from django.db import models
import os

def get_file_extension(file):
    base_name = os.path.basename(file)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image(instance, filename):
    rand_name = random.randint(1, 999999999)
    name, ext = get_file_extension(filename)
    final_name = f"{instance.id}{instance.title}-{rand_name}{ext}"
    return f"products/{filename}"


class ProductManageObjects(models.Manager):
    def get_product_by_id(self, productID):
        qs = self.get_queryset().filter(id=productID)
        if qs.count() == 1:
            return qs.first()
        return None

    def get_active_products(self):
        return self.get_queryset().filter(active=True)


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    image = models.ImageField(upload_to="upload_image", null=True, blank=True)
    active = models.BooleanField(default=False)
    # date_create = models.DateTimeField(auto_now_add=True)

    objects = ProductManageObjects()

    def __str__(self):
        return self.title

