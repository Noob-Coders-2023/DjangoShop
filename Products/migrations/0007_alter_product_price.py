# Generated by Django 5.0.1 on 2024-01-30 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0006_product_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(verbose_name='قیمت'),
        ),
    ]
