from django.db import models
from django.db.models.signals import pre_save

from Products.models import Product
from .utils import unique_slug_generator


# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    slug = models.SlugField(verbose_name='عنوان در آدرس URL', blank=True, unique=True)
    active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')
    time = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, blank=True, verbose_name='محصولات')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'برچسب / تگ'
        verbose_name_plural = 'برچسب ها / تگ ها'


def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(tag_pre_save_receiver, sender=Tag)
