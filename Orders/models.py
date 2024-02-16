from django.db import models
from django.contrib.auth.models import User

from Products.models import Product


# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
    paid = models.BooleanField(default=False, verbose_name="پرداخت شده/نشده")
    paid_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = "سبد خرید"
        verbose_name_plural = "سبدهای خرید"

    def __str__(self):
        return self.user.get_full_name()


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="سفارش")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول")
    count = models.IntegerField(default=0, verbose_name="تعداد")
    price = models.IntegerField(default=0, verbose_name="قیمت")

    class Meta:
        verbose_name = "جزئیات سبد خرید"
        verbose_name_plural = "جزئیات سبدهای خرید"

    def __str__(self):
        return self.product.title
