# Generated by Django 5.0.1 on 2024-01-20 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tags', '0002_alter_tag_options_alter_tag_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(blank=True, unique=True, verbose_name='عنوان در آدرس URL'),
        ),
    ]
