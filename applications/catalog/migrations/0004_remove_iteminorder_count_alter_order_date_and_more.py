# Generated by Django 4.1.2 on 2022-11-14 05:36

import catalog.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iteminorder',
            name='count',
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата заявки'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo_file',
            field=models.ImageField(blank=True, max_length=254, null=True, upload_to=catalog.models.get_name_file, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'bmp'])]),
        ),
    ]