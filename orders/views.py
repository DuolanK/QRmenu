from django.shortcuts import render
from .models import OrderItem, Order
#from .forms import OrderCreateForm
from cart.cart import Cart
from shop.forms import UserLoginForm


def order_create(request):
    cart = Cart(request)
    if request.user.is_authenticated:
        order = Order()
        order.save(force_insert=True)
        for item in cart:
            OrderItem.objects.create(order=order,
                                    product=item['product'],
                                    price=item['price'],
                                    quantity=item['quantity'])
            # очистка корзины
        cart.clear()
        return render(request, 'orders/order/created.html',
                          {'order': order})

    else:
        form = UserLoginForm
    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})


