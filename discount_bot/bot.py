import logging
from aiogram import Bot, Dispatcher, executor, types
from Discount_Monitoring.settings import BOT_TOKEN


logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome_message(message: types.Message):
    await message.reply('Привет!')
    
    

executor.start_polling(dp, skip_updates=True)