from django.urls import path
from django.contrib.auth import views as auth_views
from catalog.views import *

urlpatterns = [
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),

    path('', catalog, name='catalog'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),


    path('orders', OrderListView.as_view(), name='orders'),
    path('orderCreate', order_view, name='order_create'),
    path('delete_order/<pk>', delete_order, name='delete_order'),
    path('checkout', checkout, name='checkout'),
]
