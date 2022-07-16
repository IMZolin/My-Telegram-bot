import telebot
from config import TOKEN
bot = telebot.TeleBot(TOKEN)
resume = open('documents/resume.pdf','rb')
@bot.message_handler(commands=["start"])
def start_message(message):
    mess = f'Hello, <b>{message.from_user.first_name} {message.from_user.last_name}</b>! This is official Ivan Zolin`s Telegram bot. \nEnter the /help command to find out what this bot can do'
    bot.send_message(message.chat.id, mess, parse_mode='html')
@bot.message_handler(commands=["help"])
def help_message(message):
    bot.send_message(message.chat.id,'/info - to find out main info \n/socialnetowk - to view Ivan Zolin`s social networks \n/cv - to download Ivan Zolin`s CV')
@bot.message_handler(commands=["info"])
def info_message(message):
    bot.send_message(message.chat.id,'Ivan Zolin was born in Kemerovo, Russia on 06.09.2002 \nHe graduated from secondary school 92 Kemerovo. \nHe studied at Peter the Great St. Petersburg University at the Department of Applied Mathematics and Computer Science in the specialty of system programming. \nHe enjoys piano, reading books, programming, running and learning something new from mathematics, computer science and other sciences, as well as fields.')
@bot.message_handler(commands=["cv"])
def cv_message(message):
    bot.send_document(message.chat.id,resume)
@bot.message_handler(commands=["socialnetowk"])
def socialnetowk_message(message):
    bot.send_message(message.chat.id,'Github: https://github.com/IMZolin \nTwitter: https://twitter.com/zolin5269 \nLinkedin: https://www.linkedin.com/in/ivan-zolin-4474b0233/')
@bot.message_handler(content_types=['text'])
def message_reply(message):
    if (message.text == "Старт" or message.text == "Start" or message.text == "start" or message.text == "старт"):
        start_message(message)
    elif(message.text == "Help" or message.text == "Помощь" or message.text == "Хэлп" or message.text == "help" or message.text == "хэлп" or message.text == "хелп" or message.text == "хелп ми" or message.text == "хэлп ми" or message.text == "help me"):
        help_message(message)
    elif(message.text == "Резюме" or message.text == "резюме" or message.text == "Resume" or message.text == "resume" or message.text == "cv" or message.text == "Cv" or message.text == "CV"):
        cv_message(message)
    elif(message.text == "Соцсети" or message.text == "соцсети" or message.text == "Социальные сети" or message.text == "социальные сети" or message.text == "social network" or message.text == "social networks" or message.text == "Social network" or message.text == "Social networks"):
        socialnetowk_message(message)
    else:
        bot.send_message(message.chat.id, 'Try entering the command again')

if __name__ == '__main__':
    bot.polling(none_stop=True)

