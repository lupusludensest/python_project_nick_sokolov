from django.db import models

# 1
class Client(models.Model): # Starts from the capital letter and always singular
    class Meta:
        db_table = 'clients'
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
    first_name = models.CharField(blank=False, null=False, max_length=60, editable=True, verbose_name='First name')
    last_name = models.CharField(blank=False, null=False, max_length=60, editable=True, verbose_name='Last name')
    email = models.EmailField(blank=False, null=False, max_length=60, editable=True, verbose_name='Email')
    address = models.CharField(blank=False, null=False, max_length=40, editable=True, verbose_name='Address')
    city = models.CharField(blank=False, null=False, max_length=80, editable=True, verbose_name='City')
    state = models.CharField(blank=False, null=False, max_length=50, editable=True, verbose_name='State')
    country = models.CharField(blank=False, null=False, max_length=40, editable=True, verbose_name='Country')
    postal_code = models.CharField(blank=False, null=False, max_length=5, editable=True, verbose_name='Postal code')

