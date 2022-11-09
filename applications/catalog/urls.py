from django.urls import path

from catalog import views
from django.contrib.auth import views as auth_views

from catalog.views import catalog, about, contact, product, applications, checkout

urlpatterns = [
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LoginView.as_view(), name='logout'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('', catalog, name='catalog'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('product/<pk>', product, name='product'),
    path('applications', applications, name='applications'),
    path('checkout', checkout, name='checkout'),
]
