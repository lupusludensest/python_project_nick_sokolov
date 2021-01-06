from django.db import models
from clients.models import Client
from products.models import Product

# 1
class Order(models.Model):
    class Meta:
        db_table = 'orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
    client = models.ForeignKey(Client, blank=False, null=False, verbose_name='Client', on_delete=models.CASCADE)
    date = models.DateField(blank=False, null=False, editable=True, verbose_name='Data')
    pyment_method = models.CharField(blank=False, null=False, max_length=20, editable=True, verbose_name='Payment method')
    delivery_method = models.CharField(blank=False, null=False, max_length=30, editable=True, verbose_name='Delivery method')
    delivery_date = models.DateField(blank=False, null=False, editable=True, verbose_name='Delivery date')
    total_price = models.FloatField(blank=False, null=False, editable=True, verbose_name='Total price')

# 2
class Cart(models.Model):
    class Meta:
        db_table = 'carts'
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'
    order = models.ForeignKey(Order, blank=False, null=False, verbose_name='Order', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=False, null=False, verbose_name='Product', on_delete=models.CASCADE)
    date = models.DateField(blank=False, null=False, editable=True, verbose_name='Data')
    item_price = models.FloatField(blank=False, null=False, editable=True, verbose_name='Item price')
    product_quantity = models.IntegerField(blank=False, null=False, editable=True, verbose_name='Product quantity')
    sub_total = models.FloatField(blank=False, null=False, editable=True, verbose_name='Total spent')

