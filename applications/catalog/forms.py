from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from catalog.models import User


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(label='Логин',
                               validators=[RegexValidator('^[a-zA-Z-]+$',
                                                          message="Разрешены только латиница и тире")],
                               error_messages={
                                   'required': 'Обязатльное поле',
                                   'unique': 'Данный логин занят',
                               })

    email = forms.EmailField(label='Адрес электронной почты',
                             error_messages={
                                 'invalid': 'не правильный формат адреса',
                                 'unique': 'Данный адрес занят',
                             })

    password = forms.CharField(label='пароль ',
                               widget=forms.PasswordInput,
                               error_messages={
                                   'required': 'Обязательное поле',
                               })

    password2 = forms.CharField(label='пароль (повторно)',
                                widget=forms.PasswordInput,
                                error_messages={
                                    'required': 'Обязательное поле',
                                })

    rules = forms.BooleanField(required=True,
                               label='Согласие на обработку персональных данных',
                               error_messages={
                                   'required': 'Обязатльное поле',
                               })

    name = forms.CharField(label='Имя',
                           validators=[RegexValidator('^[а-яА-Я- ]+$',
                                                      message="только кириллические буквы, дефис и пробелы")],
                           error_messages={
                               'required': 'Обязатльное поле',
                           })

    surname = forms.CharField(label='Фамилия',
                              validators=[RegexValidator('^[а-яА-Я- ]+$',
                                                         message="только кириллические буквы, дефис и пробелы")],
                              error_messages={
                                  'required': 'Обязатльное поле',
                              })

    patronymic = forms.CharField(label='Отчество',
                                 validators=[RegexValidator('^[а-яА-Я- ]+$',
                                                            message="только кириллические буквы, дефис и пробелы")])

    def clean(self):
        super().clean()
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise ValidationError({
                'password2': ValidationError('Введенные пароли не совпадают', code='password_nisnatch')
            })

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2', 'name', 'surname', 'patronymic', 'rules')
