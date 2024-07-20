import telebot

from telebot.types import InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup

bot = telebot.TeleBot('7494162357:AAEN-5rbXBoLFNgxpAkOsJoM_klHQpy083g')

#define and adding buttons
btn1 = InlineKeyboardButton(text="Google", url='http://google.com')
btn2 = InlineKeyboardButton(text="Bing", url='http://bing.com')
btn3 = InlineKeyboardButton(text="btn3", callback_data='btn3')
btn4 = InlineKeyboardButton(text="btn4", callback_data='btn4')
inline_Keyboard = InlineKeyboardMarkup(row_width=1)
inline_Keyboard.add(btn1,btn2,btn3,btn4)

#reply keyboard
reply_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
reply_keyboard.add("rep_btn1","rep_btn2")

# Massage handlers
@bot.message_handler(commands=['start'])
def Hello(massage):
    #bot.send_message(massage.chat.id, 'Hello')
    bot.reply_to(massage, 'Hello, What is  your name?',reply_markup=reply_keyboard)
    bot.register_next_step_handler(massage, process_name)
def process_name(massage):
    name = massage.text
    bot.send_message(massage.chat.id, f"Thanks {name}",reply_markup=inline_Keyboard)

#Callback query handler
@bot.callback_query_handler(func=lambda call:True)
def check_button(call):
    if call.data == 'btn3':
        bot.answer_callback_query(call.id, 'You clicked btn3',show_alert=True)
    elif call.data == 'btn4':
        bot.answer_callback_query(call.id, 'You clicked btn4')

# Handling all other messages
@bot.message_handler(func=lambda massage:True)
def Check_btn(massage):
    if massage.text == "rep_btn1":
        bot.reply_to(massage, "btn1 is pressed")
    elif massage.text == "rep_btn2":
         bot.reply_to(massage, 'btn2 is pressed')
    else:
        bot.reply_to(massage, f"Your message is : {massage.text}")

bot.polling()