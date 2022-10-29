from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.crypto import get_random_string


def get_name_file(instanse, filename):
    return '/'.join([get_random_string(length=5) + '_' + filename])


class User(AbstractBaseUser):
    name = models.CharField(max_length=254, verbose_name='Имя', blank=False)
    surname = models.CharField(max_length=254, verbose_name='Фамилия', blank=False)
    patronymic = models.CharField(max_length=254, verbose_name='Отчество', blank=True)
    username = models.CharField(max_length=254, verbose_name='Логин', unique=True, blank=False)
    email = models.CharField(max_length=254, verbose_name='Почта', unique=True, blank=False)
    password = models.CharField(max_length=254, verbose_name='Пароль', blank=False)
    role = models.CharField(max_length=254, verbose_name='Роль',
                            choices=(('admin', 'Администратор'), ('user', 'Пользователь')), default='user')

    def __str__(self):
        return self.name


class Applications(models.Model):
    STATUS_CHOICES= [
        ('new', '«Новая»'),
        ('confirmed', 'Принято в работу'),
        ('canceled', 'Выполнено')
    ]
    name = models.CharField(max_length=254, verbose_name='Имя', blank=False)
    status = models.CharField(max_length=254, verbose_name='Статус', choices=STATUS_CHOICES, default='new')
    description = models.CharField(max_length=500, verbose_name='Описание', blank=False)
    category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.CASCADE)
    photo = models.ImageField(max_length=254, upload_to=get_name_file,
                              null=True, blank=True,
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'bmp'])])


class Category(models.Model):
    name = models.CharField(max_length=254, verbose_name='наименование', blank=False)

    def __str__(self):
        return self.name
