import telebot
from template.token.config import token
from telebot import types
import template.answersBot.text as text
import menu

bot = None
keyboardSys = None
if token:
    bot = telebot.TeleBot(token)
    keyboardSys = menu.KeyBoardSystem(bot)
    keyboardSys2 = menu.KeyBoardSystem(bot)


name_dish = {"Азиатская кухня": 
                {
                    "Японский карри":["морковь","лук","картошка","специальный кубик карри","курица","рис","кунжут"],
                    "Удон": ["морковь","лук","болгарский красный перец","огурец","курица","лапша удон","соус терияки","кунжут"]
                },
            "Итальянская кухня": 
                {
                    "Паста 'Болоньезе'":["морковь","лук","спагетти","фарш","зелень(на выбор: кинза, петрушка, базилик)","чеснок", "консервированные помидоры в собственном соку ", "тертый твердый сыр"],
                },
            "Русская кухня": 
                {
                    "Борщ":["морковь","лук","свекла","капуста","картошка","кость (куринная, говяжая, свинная на выбор)"],
                }
}

def filter_kitchen():
    keys_list_name_kitchen = list(name_dish.keys())
    print(keys_list_name_kitchen)


@bot.message_handler(commands=["start"])
def start(message):
    keyboardSys.createDefaultButtons(message, text)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == 'ЧТО ты можешь, БОТ?':
        bot.send_message(chat_id=message.chat.id, text=text.about_bot)
    elif message.text == 'Подбери рецепт!':
        keyboardSys.menuChoiseKitchen(message, text)


@bot.message_handler(content_types=["text"])
def echo_answer(message):
    bot.send_message(message.chat.id, message.text)

if __name__=='__main__' and bot:
    bot.infinity_polling()


