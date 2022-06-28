from django.db import models
from shop.models import Product
from django.utils.timezone import datetime

class Order(models.Model):
    def get_num(date=datetime.now()):
        date = date.strftime('%Y%m%d')
        if Order.objects.all().last():
            last_order = Order.objects.all().last()
            if last_order.number[0:8] == date:
                num = int(last_order.number[8::]) + 1
            else:
                num = 1
        else:
            return f'{date}1'
        return (f'{date}{num}')

    number = models.CharField(max_length=12, default=get_num, verbose_name='номер заказа')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity