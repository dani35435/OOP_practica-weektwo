# Generated by Django 4.1.2 on 2022-11-15 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_order_photo_file_alter_product_photo_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iteminorder',
            name='product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
