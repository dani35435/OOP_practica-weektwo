from django.urls import path

# from catalog import views
from django.contrib.auth import views as auth_views

from catalog.views import *

urlpatterns = [
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),

    path('', catalog, name='catalog'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('product/<pk>', product, name='product'),

    path('orders', OrderListView.as_view(), name='orders'),
    path('checkout', checkout, name='checkout'),
]
