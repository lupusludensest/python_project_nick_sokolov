from django.db import models

# Create your models here. Description of our structure of data in the database

class EmailCollector(models.Model):
    class Meta:
        db_table = 'emails' # name of the table in the database
        verbose_name = 'email'
        verbose_name_plural = 'emails'
    first_name = models.CharField(max_length=20, blank=False, null=False, verbose_name='First Name')
    last_name = models.CharField(max_length=20, blank=False, null=False, verbose_name='Last Name')
    department_name = models.CharField(max_length=20, blank=False, null=False, verbose_name='Department Name')
    salary = models.FloatField(max_length=20, blank=False, null=False, verbose_name='Salary')
    email = models.EmailField(max_length=70, blank=False, null=False, verbose_name='E-mail')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Time of creation')
    phone_num = models.CharField(max_length=20, blank=False, null=False, unique=True, verbose_name='Phone Number')
