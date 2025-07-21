import telebot
import schedule
import time
import threading
import json

BOT_TOKEN = '7278187669:AAHW2iU0dPF6mexFs6XlJVtC2rmTYOTD2rY'  # ← сюда вставь свой токен

bot = telebot.TeleBot(BOT_TOKEN)

# Загрузка сообщений из файла
def load_messages():
    try:
        with open('messages.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except:
        return {}

def send_messages():
    messages = load_messages()
    for group_id, text in messages.items():
        try:
            bot.send_message(group_id, text)
        except Exception as e:
            print(f"Ошибка при отправке в {group_id}: {e}")

# Планировщик на 9:00
def schedule_job():
    schedule.every().day.at("09:00").do(send_messages)
    while True:
        schedule.run_pending()
        time.sleep(1)

# Запускаем планировщик в отдельном потоке
threading.Thread(target=schedule_job).start()

# Если ты хочешь использовать команды бота — можно расширить здесь
bot.polling(none_stop=True)
