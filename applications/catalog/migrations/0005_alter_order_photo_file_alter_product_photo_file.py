# Generated by Django 4.1.2 on 2022-11-15 05:14

import catalog.utilities
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_order_commented_order_imageses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='photo_file',
            field=models.ImageField(blank=True, max_length=254, null=True, upload_to=catalog.utilities.get_timestamp_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'bmp'])]),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo_file',
            field=models.ImageField(blank=True, max_length=254, null=True, upload_to=catalog.utilities.get_timestamp_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'bmp'])]),
        ),
    ]