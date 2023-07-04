from time import sleep
from clothes.celery import app
from .models import RSSSubs
from .bot import send_message_to_all_users_by_telegram

@app.task
def add_two_numbers(a: int, b: int) -> int:
    sleep(5)
    return a + b


@app.task
def send_message_to_user_tg_task():
    message = 'Привет, на эти выходные есть супер скидки на одежду'
    users = RSSSubs.objects.all().values_list('id', flat=True)
    send_message_to_all_users_by_telegram(message, users)


# 1. Нужно сделать функцию, которая будет записывать в csv файл
# 2. Нужно получить данные с модели Clothes, где ClothesInStock.clothes_count = 0
# 3. Нужно записать в файл данные из пункта 2

# send_message_to_user.delay() # запуск задачи в селери
# send_message_to_user()  обычный запуск