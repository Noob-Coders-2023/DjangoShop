# Generated by Django 5.0.1 on 2024-02-18 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0009_alter_productgallery_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=False, verbose_name='محصول ویژه'),
        ),
    ]