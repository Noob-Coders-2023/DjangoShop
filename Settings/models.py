import random

from django.db import models
from Products.models import get_file_extension


# Create your models here.


def upload_image(instance, filename):
    rand_name = random.randint(1, 999999999)
    name, ext = get_file_extension(filename)
    final_name = f"{rand_name}{ext}"
    return f"setting/{final_name}"


class Settings(models.Model):
    email = models.EmailField(verbose_name='ایمیل')
    phone = models.CharField(max_length=200, verbose_name='تلفن تماس')
    mobile = models.CharField(max_length=150, verbose_name='شماره همراه')
    fax = models.CharField(max_length=150, verbose_name='شماره فکس')
    address = models.CharField(max_length=250, verbose_name='آدرس')
    copy_right = models.CharField(max_length=250, verbose_name='متن کپی رایت')
    about = models.TextField(verbose_name='درباره ما')
    instagram = models.CharField(max_length=250, verbose_name='آدرس صفحه اینستراگرام')
    logo = models.ImageField(upload_to=upload_image, null=True, blank=True, verbose_name='تصویر')

    class Meta:
        verbose_name = 'تنظیمات'
        verbose_name_plural = 'تنظیمات'
