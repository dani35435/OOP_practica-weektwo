from django.urls import path
from catalog import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LoginView.as_view(), name='logout'),
    path('register', views.RegisterView.as_view(), name='register'),
]