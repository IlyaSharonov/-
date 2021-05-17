from app import bot, dp
from aiogram.types import Message
from config import admin_id, todo, HELP

import time

uDate, uTask = 0, 0
reqv = 0
"""
0 - ожидание команды
1 - ожидание даты
2 - ожидание задачи
3 - ожидание даты для команды done
4 - удаление элемента при выборе
"""

async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text="Бот запущен!")

@dp.message_handler(commands=["start"])
async def start(message:Message):
    await message.answer(text="Работает")

@dp.message_handler(commands=["add"])
async def add(message:Message):
    global reqv
    await message.answer(text="Введите дату")
    reqv = 1

@dp.message_handler(commands=["show"])
async def show(message:Message):
    for date in sorted( todo.keys() ): #проходим по ключам
        for task in todo[ date ]: #проходим по списку задач
            await message.answer(text = f"[{date}] - {task}")


@dp.message_handler(commands=["done"])
async def done(message:Message):
    global reqv
    await message.answer(text="Введите дату")
    reqv = 3

@dp.message_handler(commands=["help"])
async def help(message:Message):
    await message.answer(text=HELP)


@dp.message_handler()
async def echo(message:Message):
    global reqv, uDate, uTask, todo

    if reqv == 1:
        uDate = message.text
        try:
            time.strptime(uDate, "%d.%m.%Y") # 12.02.2021
        except ValueError:
            await message.answer(text = "не верный формат даты")
            reqv = 0
            return
        await message.answer(text = "Что нужно сделать?")
        reqv = 2
    elif reqv == 2:
        uTask = message.text
        if uDate in todo:
            todo[ uDate ].append( uTask )
        else:
            todo[ uDate ] =  uTask 
        await message.answer(f"Добавлена задача '{uTask}' на {uDate} ")
        reqv = 0
    elif reqv == 3:
        uDate = message.text
        try:
            time.strptime(uDate, "%d.%m.%Y") # 12.02.2021
        except ValueError:
            await message.answer(text = "не верный формат даты")
            reqv = 0
            return
        
        if uDate in todo:
            if len( todo[ uDate ] ) == 1:
                tmp = todo.pop(uDate)
                await message.answer(f"Задача '{tmp}' - удалена")
            else:
                await message.answer("Какую задачу удалить?")
                tmp = 1
                for task in todo[ uDate ]:
                    await message.answer(f"[{tmp}] - {task}")
                    tmp += 1
                reqv = 4
        else:
            await message.answer("Не задач на эту дату")
            reqv = 0
    elif reqv == 4:
        try:
            int(message.text)
        except ValueError:
            await message.answer("Не верный формат команды")
            reqv = 0
            return
        if len( todo[ uDate ] ) >= int(message.text):
            await message.answer(f"Задача '{todo[uDate].pop(int(message.text)-1)}' - удалена")
            reqv = 0
        else:
            await message.answer("Нет такой команды")
            reqv = 0
