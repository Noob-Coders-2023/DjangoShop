import os
import random
from Products.models import get_file_extension, upload_image

from django.db import models


# Create your models here.


class Slider(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان اسلایدر')
    link = models.URLField(max_length=200, verbose_name='لینک')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to=upload_image, null=True, blank=True, verbose_name='تصویر')
    active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدرها'

    def __str__(self):
        return self.title
