import requests,user_agent,json,flask,telebot,random,os,sys
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)

def Ch_id(id):
    ch = False
    file = open("users.txt",'r')
    for line in file:
        if str(line.strip()) == str(id):
            ch = True
    file.close()
    return ch
@bot.message_handler(commands=['start'])
def boten(message):
    ch = '@dtdtdt'
    sudo_id = "1372680721"
    token=Token
    idd = message.from_user.id
    url = f"https://api.telegram.org/bot{token}/getchatmember?chat_id={ch}&user_id={idd}"
    req = requests.get(url)
    if idd == sudo_id or 'member' in req.text or 'creator' in req.text or 'administartor' in req.text:
        idu = message.from_user.id
        nam = message.from_user.first_name
        us = message.from_user.username
        id_user = str(message.from_user.id)
        ck = Ch_id(str(id_user))
        if ck == False:
            file =open ("users.txt", "a").write(str(id_user)+"\n")
            file_users = open("users.txt",'r').readlines()
            users = len(file_users)
            ide = "1372680721"
            fg = bot.send_message(ide,f"""تم دخول شخص جديد :{users}
    	        ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
    	        ❂ - 𝚄𝚂𝙴𝚁 ⟿ @{us} 🤍..
    	        ❂ - 𝙸𝙳 𝚂𝚃𝙰 ⟿ {idu} 🤍.  
    	        ❂ - NAME 𝚂𝚃𝙰 ⟿ {nam} 🤍.  
    	        ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉	        
    	        """)    
        Id =message.chat.id
        Name = message.chat.first_name
        User = message.from_user.username
        A = types.InlineKeyboardMarkup(row_width = 3)
        B = types.InlineKeyboardButton(text = "info username insta",callback_data = "A")
        C = types.InlineKeyboardButton(text = "Get SessionId",callback_data = "insta0")
        #mm = types.InlineKeyboardButton(text = "أضفني الى مجموعتك↗️",url = "https://t.me/DtDtDtBot?startgroup=text")
        A.add(B,C)
    
        bot.send_message(message.chat.id,"""
    *➖ 👋اهلا عزيزي *  [{}]""".format(Name),parse_mode="markdown",reply_markup=A)
    else:
        A = types.InlineKeyboardMarkup(row_width = 1)
        B = types.InlineKeyboardButton(text = '''"𝙰𝙻𝙾𝚂𝙷"𝙿𝚈𝚃𝙷𝙾𝙽"''',url="https://t.me/DtDtDt")
        A.add(B)
        bot.send_message(message.chat.id, """*🚸| عذرا عزيزي
🔰| عليك الاشتراك بقناة البوت لتتمكن من استخدامه

- مــعرف القـناة : {} 

‼️| اشترك ثم ارسل /start*""".format(ch),parse_mode="markdown",reply_markup=A)

@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://pythonaali.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
