from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from catalog.models import User, Order


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'required': False}),
                               validators=[RegexValidator('^[a-zA-Z0-9-]+$',
                                                          message="Разрешены только латиница, цифры или тире")],
                               error_messages={
                                   'invalid': 'Не правильный формат адреса',
                                   'required': 'Поле для заполнение обязательно',
                                   'unique': 'Данный логин занят'
                               }),

    email = forms.EmailField(label='Адрес электронной почты',
                             error_messages={
                                 'invalid': 'Не правильный формат адреса',
                                 'unique': 'Данный адрес занят'
                             })
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput,
                               error_messages={
                                   'required': 'Обязательное поле',
                               })
    password2 = forms.CharField(label='Пароль (повторно)',
                                widget=forms.PasswordInput,
                                error_messages={
                                    'required': 'Обязательное поле',
                                })
    rules = forms.BooleanField(required=False,
                               label='Согласие с правилами регистрации',
                               error_messages={
                                   'required': 'Обязательное поле',
                               })
    name = forms.CharField(label='Имя',
                           validators=[RegexValidator('^[а-яА-Я- ]+$',
                                                      message="Разрешены только кирилица, пробел или тире")],
                           error_messages={
                               'required': 'Обязательное поле'
                           })
    surname = forms.CharField(label='Фамилия',
                              validators=[RegexValidator('^[а-яА-Я- ]+$',
                                                         message="Разрешены только кирилица, пробел или тире")],
                              error_messages={
                                  'required': 'Обязательное поле'
                              })
    patronymic = forms.CharField(label='Отчество',
                                 validators=[RegexValidator('^[а-яА-Я- ]+$',
                                                            message="Разрешены только кирилица, пробел или тире")])

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].required = False
        self.fields['email'].required = False
        self.fields['password'].required = False
        self.fields['password2'].required = False
        self.fields['rules'].required = False
        self.fields['name'].required = False
        self.fields['surname'].required = False
        self.fields['patronymic'].required = False


    def clean(self):
        super().clean()
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise ValidationError({
                'password2': ValidationError('Введенные пароли не совпадают', code='password_mismatch')
            })

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2',
                  'name', 'surname', 'patronymic', 'rules')


class OrderCreate(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'descriptions', 'category', 'photo_file')


class OrderForm(forms.ModelForm):
    def clean(self):
        status = self.cleaned_data.get('status')
        imageses = self.cleaned_data.get('imageses')
        commented = self.cleaned_data.get('commented')
        if self.instance.status != 'new':
            raise forms.ValidationError({'status': 'Статус можно изменить только у новых заказов'})
        if status == 'confirmed' and not imageses:
            raise forms.ValidationError({'status': 'Статус можно изменить только добавив картинку'})
        if status == 'canceled' and not commented:
            raise forms.ValidationError({'status': 'Статус можно изменить только добавив коментарий'})
