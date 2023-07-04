import requests
from telebot import TeleBot

from .models import RSSSubs

BOT_TOKEN ='5947621004:AAHOH9iDAqxzstwfqIVmmYnkY7cptiMYfSI'

bot = TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я бот, который поможет тебе найти одежду. Вы успешно подписались на рассылку')

    RSSSubs.objects.get_or_create(
        telegram_id = message.chat.id,
        name = message.chat.first_name
    )


def send_message_to_all_users_by_telegram(message: str, users: list):
    users_queryset = RSSSubs.objects.filter(id__in=users)
    for user in users_queryset:
        bot.send_message(user.telegram_id, message)

if __name__ == '__main__':
    bot.polling(non_stop=True)