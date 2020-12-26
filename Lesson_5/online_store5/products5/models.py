from django.db import models

class Product(models.Model):
    class Meta:
        db_table = 'products5'
        verbose_name = 'Good'
        verbose_name_plural = 'Goods'

    title = models.CharField(blank=False, null=False, max_length=200, verbose_name='Title')
    price = models.FloatField(blank=False, null=False, verbose_name='Price')


class Category(models.Model):
    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    title = models.CharField(blank=False, null=False, max_length=200, verbose_name='Title')


class ProductCategory(models.Model):
    class Meta:
        db_table = 'products_categories'
        verbose_name = 'Product category'
        verbose_name_plural = 'Product categories'

    product = models.ForeignKey(Product, blank=False, null=False, verbose_name='Good', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, blank=False, null=False, verbose_name='Category', on_delete=models.CASCADE)