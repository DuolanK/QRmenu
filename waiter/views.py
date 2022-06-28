from django.shortcuts import render
from orders.models import OrderItem



def waiter(request):
    orderitem = OrderItem.objects.all()
    return render(request, 'waiter/waiter.html', {'orderitem': orderitem})