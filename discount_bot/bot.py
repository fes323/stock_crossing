import logging
from shops.models import Shop
import telebot
from datetime import datetime, timedelta
from Discount_Monitoring.settings import BOT_TOKEN
from discount.models import DiscountData
from django.db.models import Count


bot=telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['discount'])
def start_message(message):
    now = datetime.now()
    discountCurrent = DiscountData.objects.filter(startDate__lte=now).filter(endDate__gte=now).order_by('-startDate')
    bot.send_message(message.chat.id, f"Привет ✌️/n Список акций: {discountCurrent}")

@bot.message_handler(commands=['count'])
def start_message(message):
    now = datetime.now()
    allCurrentDiscountCounter = DiscountData.objects.filter(startDate__lte=now).filter(endDate__gte=now).count()
    bot.send_message(message.chat.id, f"Количество действующих акций:  {allCurrentDiscountCounter}")
    
@bot.message_handler(commands=['top'])
def start_message(message):
    allShops = Shop.objects.all()
    topByNumberOfDiscount = allShops.annotate(num_discount=Count('shop')).order_by('-countCurrentDiscount')
    bot.send_message(message.chat.id, f"Топ сетей по количеству действующих акций:  {topByNumberOfDiscount}")
    
@bot.message_handler(commands=['download'])
def start_message(message):
    allShops = Shop.objects.all()
    topByNumberOfDiscount = allShops.annotate(num_discount=Count('shop')).order_by('-countCurrentDiscount')
    bot.send_message(message.chat.id, f"Топ сетей по количеству действующих акций:  {topByNumberOfDiscount}")
  
bot.infinity_polling()

