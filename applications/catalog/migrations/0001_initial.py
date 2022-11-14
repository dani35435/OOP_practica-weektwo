# Generated by Django 4.1.2 on 2022-11-14 05:02

import catalog.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=254, verbose_name='Имя')),
                ('surname', models.CharField(max_length=254, verbose_name='Фамилия')),
                ('patronymic', models.CharField(blank=True, max_length=254, verbose_name='Отчество')),
                ('username', models.CharField(max_length=254, unique=True, verbose_name='Логин')),
                ('email', models.CharField(max_length=254, unique=True, verbose_name='Почта')),
                ('password', models.CharField(max_length=254, verbose_name='Пароль')),
                ('role', models.CharField(choices=[('admin', 'Администратор'), ('user', 'Пользователь')], default='user', max_length=254, verbose_name='Роль')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, verbose_name='Наименование')),
            ],
        ),
        migrations.CreateModel(
            name='ItemInOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0, verbose_name='Количество')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, verbose_name='Имя')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('photo_file', models.ImageField(blank=True, max_length=254, null=True, upload_to=catalog.models.get_name_file, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')),
                ('status', models.CharField(choices=[('new', 'Новый'), ('confirmed', 'Подтвержденный'), ('canceled', 'Отмененный')], default='new', max_length=254, verbose_name='Статус')),
                ('products', models.ManyToManyField(related_name='orders', through='catalog.ItemInOrder', to='catalog.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.AddField(
            model_name='iteminorder',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.order', verbose_name='Заказ'),
        ),
        migrations.AddField(
            model_name='iteminorder',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='Товар'),
        ),
    ]
