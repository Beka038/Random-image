import telebot
from config import TOKEN
import random
import os
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import requests

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['star'])
def starting(message): 
    keyboard = ReplyKeyboardMarkup()
    btn1 = KeyboardButton('/mem')
    keyboard.add(btn1)
    bot.send_message(message.chat.id, 'Привет гапиши мне команду /mem', reply_markup=keyboard)
    
    
@bot.message_handler(commands=['mem'])
def meme(message):
    image = random.choice(os.listdir('img'))
    with open(f'img/{image}', 'rb') as f:
        bot.send_photo(message.chat.id, f)
    

def dog_image():
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

def cat_image():
    url = 'https://api.thecatapi.com/v1/images/search'
    res = requests.get(url)
    data = res.json()
    return data[0]['url']

def fox_image():
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['image']

@bot.message_handler(commands=['image'])
def dog__image(message):
    url_image = dog_image()
    bot.send_message(message.chat.id, url_image)
    
def random_image():
    random_img = [cat_image(), dog_image(), fox_image()]
    return random.choice(random_img)

@bot.message_handler(commands = ['img'])
def random_picture(message):
    url_img = random_image()
    bot.send_message(message.chat.id, url_img)

bot.infinity_polling()
