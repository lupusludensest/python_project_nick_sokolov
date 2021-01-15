from django.db import models

class Subscriber(models.Model):
    class Meta:
        db_table = 'subscribers'
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'

    first_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='First name')
    last_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Last name')
    user_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='User name')
    telegram_id = models.BigIntegerField(blank=False, null=False, verbose_name='Telegram ID')


class Message(models.Model):
    class Meta:
        db_table = 'messages'
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    sending_time = models.DateTimeField(blank=True, null=True, verbose_name='Sending time')
    is_sent = models.BooleanField(default=False, verbose_name='Is sent')
    message_text = models.TextField(max_length=999, blank=False, null=False, verbose_name='Message text')




