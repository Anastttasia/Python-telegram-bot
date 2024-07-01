import telebot
from telebot import types


class BUTTON_TYPES:
    ABOUT = types.KeyboardButton('ЧТО ты можешь, БОТ?')
    CHOSE_RECIEPT = types.KeyboardButton('Подбери рецепт!')

    ASIAN_KITCHEN = types.KeyboardButton('Азиатская🍜')
    ITALIAN_KITCHEN = types.KeyboardButton('Итальянская🍝')
    RUSSIAN_KITCHEN = types.KeyboardButton('Русская🥘')

    DEFAULT_BUTTONS = (ABOUT, CHOSE_RECIEPT)
    COUNTRY_FILTER_BUTTONS = (ASIAN_KITCHEN, ITALIAN_KITCHEN, RUSSIAN_KITCHEN)


class KeyBoardSystem():
    def __init__(self, bot):
        self.__bot = bot
        self.markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    def createDefaultButtons(self, message, text):
        self.markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for button in BUTTON_TYPES.DEFAULT_BUTTONS:
            self.markup.add(button)

        self.__bot.send_message(message.chat.id, text=text.hello, reply_markup=self.markup)

    def menuChoiseKitchen(self, message, text):
        self.markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for button in BUTTON_TYPES.COUNTRY_FILTER_BUTTONS:
            self.markup.add(button)

        self.__bot.send_message(message.chat.id, text=text.choice_name_kitchen, reply_markup=self.markup)



