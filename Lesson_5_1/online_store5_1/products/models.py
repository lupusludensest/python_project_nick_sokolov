from django.db import models

# 1
class Product(models.Model): # Starts from the capital letter and always singular
    class Meta:
        db_table = 'products' # Starts from the lowercase letter and can be plural
        verbose_name = 'Product' # Starts from the capital letter and always singular
        verbose_name_plural = 'Products' # Starts from the capital letter and always plural

    product_name = models.CharField(blank=False, null=False, max_length=50, editable=True, verbose_name='Product name')
    product_brand = models.CharField(blank=False, null=False, max_length=40, editable=True, verbose_name='Product brand')
    year_of_manufacture = models.IntegerField(blank=False, null=False, editable=True, verbose_name='Year of manufacture')
    color = models.CharField(blank=False, null=False, max_length=25, editable=True, verbose_name='Color')
    description = models.TextField(blank=False, null=False, max_length=999, editable=True, verbose_name='Description')
    price = models.FloatField(blank=False, null=False, editable=True, verbose_name='Price')

# 2
class Category(models.Model):
    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    category = models.CharField(blank=False, null=False, max_length=30, editable=True, verbose_name='Category')
    description = models.TextField(blank=False, null=False, max_length=999, editable=True, verbose_name='Description')

# 3
class ProductCategory(models.Model):
    class Meta:
        db_table = 'products_categories'
        verbose_name = 'Product category'
        verbose_name_plural = 'Product categories'

    product = models.ForeignKey(Product, blank=False, null=False, verbose_name='Product', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, blank=False, null=False, verbose_name='Category', on_delete=models.CASCADE)


