from django.db import models

# 1
class Product(models.Model): # Starts from the capital leter and always singular
    class Meta:
        db_table = 'products' # Starts from the lowercase letter and can be plural
        verbose_name = 'Product' # Starts from the capital leter and always singular
        verbose_name_plural = 'Products' # Starts from the capital leter and always plural

    product_name = models.CharField(blank=False, null=False, max_length=50, editable=False, verbose_name='Product name')
    product_brand = models.CharField(blank=False, null=False, max_length=40, editable=False, verbose_name='Product brand')
    year_of_manufacture = models.IntegerField(blank=False, null=False, editable=True, verbose_name='Year of manufacture')
    color = models.CharField(blank=False, null=False, max_length=25, editable=False, verbose_name='Color')
    description = models.TextField(blank=False, null=False, max_length=999, editable=False, verbose_name='Description')
    price = models.FloatField(blank=False, null=False, editable=False, verbose_name='Price')

# 2
class Category(models.Model):
    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    category = models.CharField(blank=False, null=False, max_length=30, editable=False, verbose_name='Category')
    description = models.TextField(blank=False, null=False, max_length=999, editable=False, verbose_name='Description')

# 3
class ProductCategory(models.Model):
    class Meta:
        db_table = 'products_categories'
        verbose_name = 'Product category'
        verbose_name_plural = 'Product categories'

    product = models.ForeignKey(Product, blank=False, null=False, verbose_name='Product', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, blank=False, null=False, verbose_name='Category', on_delete=models.CASCADE)

# 4
class Client(models.Model):
    class Meta:
        db_table = 'client'
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
    first_name = models.CharField(blank=False, null=False, max_length=60, editable=False, verbose_name='First name')
    last_name = models.CharField(blank=False, null=False, max_length=60, editable=False, verbose_name='Last name')
    nick_name = models.CharField(blank=False, null=False, max_length=60, editable=False, verbose_name='Nick name')
    email = models.EmailField(blank=False, null=False, max_length=60, editable=False, verbose_name='Email')
    password = models.CharField(blank=False, null=False, max_length=25, editable=False, verbose_name='Password')
    address = models.CharField(blank=False, null=False, max_length=40, editable=False, verbose_name='Address')
    city = models.CharField(blank=False, null=False, max_length=80, editable=False, verbose_name='City')
    state = models.CharField(blank=False, null=False, max_length=50, editable=False, verbose_name='State')
    country = models.CharField(blank=False, null=False, max_length=40, editable=False, verbose_name='Country')
    postal_code = models.CharField(blank=False, null=False, max_length=5, editable=False, verbose_name='Postal code')

# 5
class Order(models.Model):
    class Meta:
        db_table = 'orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
    client = models.ForeignKey(Client, blank=False, null=False, verbose_name='Client', on_delete=models.CASCADE)
    date = models.DateField(blank=False, null=False, editable=False, verbose_name='Data')
    pyment_method = models.CharField(blank=False, null=False, max_length=20, editable=False, verbose_name='Payment method')
    delivery_method = models.CharField(blank=False, null=False, max_length=30, editable=False, verbose_name='Delivery method')
    delivery_date = models.DateField(blank=False, null=False, editable=False, verbose_name='Delivery date')
    total_price = models.FloatField(blank=False, null=False, editable=False, verbose_name='Total price')

# 6
class Cart(models.Model):
    class Meta:
        db_table = 'carts'
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'
    order = models.ForeignKey(Order, blank=False, null=False, verbose_name='Order', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=False, null=False, verbose_name='Product', on_delete=models.CASCADE)
    date = models.DateField(blank=False, null=False, editable=False, verbose_name='Data')
    item_price = models.FloatField(blank=False, null=False, editable=False, verbose_name='Item price')
    product_quantity = models.IntegerField(blank=False, null=False, editable=False, verbose_name='Product quantity')
    sub_total = models.FloatField(blank=False, null=False, editable=False, verbose_name='Total spent')



