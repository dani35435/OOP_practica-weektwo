from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView
from catalog.forms import RegisterUserForm, OrderCreate
from django.contrib.auth.decorators import login_required
from catalog.models import Order, Category


class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')


def about(request):
    return render(request, 'catalog/about.html')


def catalog(request):
    orders = Order.objects.filter(status="canceled")
    order_by = request.GET.get('order_by')
    counter = Order.objects.filter(status='confirmed').count()


    if order_by:
        orders = orders.order_by(order_by)
    else:
        orders = orders.order_by('-date')[:4]

    return render(request, 'catalog/catalog.html',
                  context={
                      'category': Category.objects.all(),
                      'orders': orders,
                      'counter': counter,
                  })


def contact(request):
    return render(request, 'catalog/contact.html')


class OrderListView(LoginRequiredMixin, generic.ListView):
    model = Order
    template_name = 'catalog/orders.html'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-date')


@login_required
def delete_order(request, pk):
    order = Order.objects.filter(user=request.user, pk=pk, status='new')
    if order:
        messages.add_message(request, messages.SUCCESS,
                             'Заявка удалена')
        order.delete()
    return redirect('orders')


@login_required
def order_view(request):
    if request.method == 'POST':
        form = OrderCreate(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author_id = request.user.pk
            order = form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Заявка создана')
            return redirect('/orders')
    else:
        form = OrderCreate(initial={'author': request.user.pk})
    context = {'form': form}
    return render(request, 'catalog/order_create.html', context)
