from typing import Any, Optional
from django.core.management.base import BaseCommand, CommandError
from Discount_Monitoring.settings import BOT_TOKEN
from discount_bot import bot
import telebot

class Command(BaseCommand):
    help = 'Start telegram bot'
    
    def handle(self, *args: Any, **options: Any) -> str | None:
        print('Запуска бота...')
        bot.start_message()
        