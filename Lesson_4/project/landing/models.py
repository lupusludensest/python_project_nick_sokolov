from django.db import models

# Create your models here.

class EmailCollector(models.Model):
    class Meta:
        db_table = 'emails' # name of the table in the database
        verbose_name = 'email'
        verbose_name_plural = 'emails'
    id = models.IntegerField(primary_key=True,blank=False, null=False, verbose_name='Id' )
    first_name = models.CharField(max_length=20, blank=False, null=False, verbose_name='First Name')
    last_name = models.CharField(max_length=20, blank=False, null=False, verbose_name='Last Name')
    email = models.EmailField(max_length=70,blank=False, null=False, verbose_name='E-mail')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Time of creation')
