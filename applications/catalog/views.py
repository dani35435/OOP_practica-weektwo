from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from catalog.forms import RegisterUserForm
from django.contrib.auth.decorators import login_required


class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')


def about(request):
    return render(request, 'catalog/about.html')


def catalog(request):
    return render(request, 'catalog/catalog.html')


def contact(request):
    return render(request, 'catalog/contact.html')


def product(request):
    return render(request, 'catalog/product.html')


@login_required
def applications(request):
    return render(request, 'catalog/applications.html')


@login_required
def checkout(request):
    return render(request, 'catalog/checkout.html')
