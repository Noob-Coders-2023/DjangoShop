import random
from django.db import models
import os

def get_file_extension(file):
    base_name = os.path.basename(file)
    name, ext = os.path.splitext(base_name)
    return name, ext
def upload_image(instance, filename):
    rand_name = random.randint(1,999999999)
    name, ext = get_file_extension(filename)
    final_name = f"{instance.id}{instance.title}-{rand_name}{ext}"
    return f"products/{filename}"


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    image = models.ImageField(upload_to="upload_image", null=True, blank=True)
    # active = models.BooleanField()
    # date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title