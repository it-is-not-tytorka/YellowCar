# клавиатура бота
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
menu = [
    [InlineKeyboardButton(text="Add image of a yellow car", callback_data="add_car"),
     InlineKeyboardButton(text="Exchange cars to hits", callback_data="exchange_cars_to_hits")],
    [InlineKeyboardButton(text="Check statistic", callback_data="get_statistic")],
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Exit from menu")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Enter to menu", callback_data="menu")]])
