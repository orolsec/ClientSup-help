import os
from io import BytesIO
import telebot
from PIL import Image, ImageDraw, ImageFont

# 1. Вставьте токен, полученный от BotFather
TOKEN = "Your_Token_Here"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Отправь мне свои ФИО, и я сгенерирую для тебя сертификат.")

@bot.message_handler(content_types=['text'])
def generate_certificate(message):
    user_name = message.text
    chat_id = message.chat.id
    
    bot.send_message(chat_id, "Генерация сертификата, пожалуйста, подождите...")

    try:
        template = Image.open("template.png")
        draw = ImageDraw.Draw(template)

        # Установленный вами размер шрифта 70
        font = ImageFont.truetype("arial.ttf", 70)

        # Вычисление центра по горизонтали
        img_width, _ = template.size
        text_width = draw.textlength(user_name, font=font)
        x = (img_width - text_width) / 2
        
        # Ваша координата Y
        y = 800 

        # Рисуем текст
        draw.text((x, y), user_name, font=font, fill="black")

        # Отправка пользователю
        output = BytesIO()
        output.name = 'certificate.jpg'
        template.save(output, format='JPEG')
        output.seek(0)
        
        bot.send_photo(chat_id, photo=output, caption="Ваш готовый сертификат!")
        output.close()

    except Exception as e:
        bot.send_message(chat_id, f"Произошла ошибка при генерации: {e}")

# Запуск бота
bot.infinity_polling()
