from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.db import models


class Employee(models.Model):
    full_name = models.CharField(max_length=64, blank=False)
    birthday = models.DateField(blank=False)

    def __str__(self) -> str:
        return self.full_name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Client(models.Model):
    full_name = models.CharField(max_length=64, blank=False)
    birthday = models.DateField(blank=False)

    def __str__(self) -> str:
        return self.full_name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Product(models.Model):
    name = models.CharField(max_length=128, blank=False)
    quantity = models.IntegerField(blank=False)
    price = models.DecimalField(blank=False, max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Order(models.Model):
    employee = models.ForeignKey(
        Employee, related_name='orders', on_delete=models.DO_NOTHING)
    client = models.ForeignKey(
        Client, related_name='orders', on_delete=models.DO_NOTHING)
    products = models.ManyToManyField(Product)
    price = models.DecimalField(
        blank=False, default=0., max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Order ID: {self.id}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


@receiver(m2m_changed, sender=Order.products.through)
def update_order_price(sender, instance, action, **kwargs):
    if action == 'post_add':
        total_price = 0
        for product in instance.products.all():
            total_price += product.price
            product.quantity -= 1
            product.save()
        instance.price = total_price
        instance.save()
