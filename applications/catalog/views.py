from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView
from catalog.forms import RegisterUserForm
from django.contrib.auth.decorators import login_required

from catalog.models import Order, Product


class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')


def about(request):
    return render(request, 'catalog/about.html')


def catalog(request):
    products = Product.objects.filter(status="canceled")[:4]
    return render(request, 'catalog/catalog.html',
                  context={'products': products})


def contact(request):
    return render(request, 'catalog/contact.html')


def product(request):
    return render(request, 'catalog/product.html')


class OrderListView(LoginRequiredMixin, generic.ListView):
    model = Order
    template_name = 'catalog/orders.html'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-date')


@login_required
def delete_order(request, pk):
    order = Order.objects.filter(user=request.user, pk=pk, status='new')
    if order:
        order.delete()
    return redirect('orders')


@login_required
def checkout(request):
    return render(request, 'catalog/checkout.html')
