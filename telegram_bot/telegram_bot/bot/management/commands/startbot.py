# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
import requests

class Command(BaseCommand):
    help = 'Test'
    def handle(self, *args, **options):
        bot_id = '1372560787:AAHKXTvwwXr3TBRjTLxcxMbGWYonFIqWZ0M'
        chat_id = '461874955'
        message = 'Hello, world!'
        base_url = 'https://api.telegram.org/bot'+bot_id+'/sendMessage?chat_id='+chat_id+'&text='+message
        requests.get(base_url)
        print(f'Message sent')

# 1372560787:AAHKXTvwwXr3TBRjTLxcxMbGWYonFIqWZ0M
# https://api.telegram.org/bot1372560787:AAHKXTvwwXr3TBRjTLxcxMbGWYonFIqWZ0M/getUpdates
# 461874955
# https://api.telegram.org/botID:HASH/sendMessage