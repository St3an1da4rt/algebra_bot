from aiogram import Bot, types, executor, Dispatcher
from keyboard import in_start, in_mater, in_mater_v, in_mater_u, in_mater_e, in_mater_f, in_mater_d, in_mater_n, \
    in_histor, pod_end, in_res, ese
from config import TOKEN
import sqlite3 as sl
import logging
import random

bot = Bot(TOKEN)
db = Dispatcher(bot)

moder_id = ['1661617508']

left_right = {'v': [1, 8],
              'u': [1, 12],
              'n': [1, 8],
              'f': [1, 5],
              'd': [1, 5],
              'e': [1, 4]
              }

exercise_base = {}
sos = {}
callback_d = ''
ses = 0
message_counter = {}
conversation_status = {}


def callback_exp(call):
    ddb = sl.connect('database2.db')
    cur = ddb.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS cold(
    cald TEXT PRIMARY KEY UNIQUE,
    text          TEXT,
    photo         TEXT,
    movie         TEXT,
    doc           TEXT,
    expert        TEXT
    )""")

    cur.execute("SELECT * FROM cold WHERE cald = ?", (call,))
    fetchall = cur.fetchall()
    sp = fetchall[0][-1].split('";"')
    mat = []
    for i in sp:
        if i is not None:

            tex = i.split('":"')
            mat.append(tex)
        else:
            mat.append(None)
    return mat


def callback_parametr(call):
    ddb = sl.connect('database2.db')
    cur = ddb.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS cold(
    cald TEXT PRIMARY KEY UNIQUE,
    text          TEXT,
    photo         TEXT,
    movie         TEXT,
    doc           TEXT,
    expert        TEXT
    )""")

    cur.execute("SELECT * FROM cold WHERE cald = ?", (call,))

    return cur.fetchall()


help_text = '''
✅Для того чтобы найти интересующий вас материал пройдите во вкладку "Материалы" там вы можете выбрать раздел и тему, 
также вы можете находить на них практичесские задачи.
↘️Для того чтобы узнать немного истории перейдите в вкладку
"История математики", только осторожно, можно встретить ❗ОЧЕНЬ ПРИОЧЕНЬ интересные факты❗. 
💬Если вы увидите ошибку
в прогамме можете написать админинстратору нажав на кнопку "Написать админу" и написать сообщение с описанием ошибки


/start - начало работы
/help - памагите
'''


@db.message_handler(commands=['start'])
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id,
                           text=f'''✅Привет {msg.from_user.full_name}!✅
🖐Вас приветствует бот - помощник по алгебре

Данный телеграмм бот предназначен для учащихся 8-х классов, изучающих алгебру на углубленном уровне.
В работе проведен анализ литературы по теме исследования. Создан чат-бот по темам алгебры 8-х классов
изучающих курс алгебры на углубленном уровне.

📖У нас есть свой учебник!
Напишите /book и вы получите документ

⚠️Напишите - /help, чтобы ознакомится с командами''',
                           reply_markup=in_start)


@db.message_handler(commands=['help'])
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, text=help_text)


@db.message_handler(commands=['book'])
async def echo_message(msg: types.Message):
    with open('творческая сессия.pdf', 'rb') as f:
        doc = f
        await bot.send_document(chat_id=msg.from_user.id, document=doc, caption='Учебник 8 класса')

@db.message_handler(lambda msg: str(msg.text).split()[0] in ["/adm"] and str(msg.from_user.id) in moder_id)
async def adm_pod(msg: types.Message):
    mat = msg.text.split()
    id_u = [int(mat[1]), 0000000000][len(mat) < 2]
    text = f"⚠️От админинстратора бота:\n{' '.join(mat[2:])}"
    await bot.send_message(id_u, text=text)


@db.message_handler(lambda msg: msg and conversation_status[msg.from_user.id] == 1)
async def podder(message):
    m = message.text
    for i in moder_id:
        await bot.send_message(i, f"Пользователь *{message.from_user.id}* '{message.from_user.full_name}' сообщил вам:\n{m}")
        await bot.send_message(message.from_user.id, f"Вы отправили админам - '{m}'")


@db.message_handler(lambda msg: msg and exercise_base[msg.from_user.id][0] == 1)
async def podder(message):
    m = message.text
    await bot.send_message(message.from_user.id, f"""Ваш ответ *{m}* принят!
Сравните ваш ответ с нашим.
Ответ: {exercise_base[message.from_user.id][1]}""", parse_mode='HTML', reply_markup=ese)



@db.callback_query_handler(text="resume3")
async def resu_back(call: types.CallbackQuery):
    ms = call.message.message_id
    for i in range(ms - message_counter[call.from_user.id] + 2, ms + 1):
        await bot.delete_message(call.from_user.id, i)


@db.callback_query_handler()
async def call_message_mater(call: types.CallbackQuery):
    try:
        global exercise_base, conversation_status, message_counter, sos
        exercise_base[call.from_user.id] = 0
        conversation_status[call.from_user.id] = 0
        global ses
        if call.data == 'histor':
            await call.message.edit_reply_markup(reply_markup=in_histor)
        elif call.data == 'resume2':
            cal = f'{sos[call.from_user.id]}_{left_right[sos[call.from_user.id]][1]}'
            matt = callback_exp(cal)
            rand = matt[random.randrange(1, len(matt))]
            await bot.send_message(call.from_user.id, rand[0])
            exercise_base[call.from_user.id] = [1, rand[1]]
        elif call.data == 'podd':
            await call.message.edit_reply_markup(reply_markup=pod_end)
            await bot.send_message(call.from_user.id,
                                   text="💬 Пишите, нажмите на кнопку ниже если нужно будет закончить разговор")
            conversation_status[call.from_user.id] = 1
        elif call.data == 'mater':
            await call.message.edit_reply_markup(reply_markup=in_mater)
        elif call.data == 'nazad1':
            await call.message.edit_reply_markup(reply_markup=in_start)
        elif call.data == 'nazad2':
            await call.message.edit_reply_markup(reply_markup=in_mater)
        elif call.data.startswith('mater_'):
            if call.data == 'mater_v':
                await call.message.edit_reply_markup(reply_markup=in_mater_v)
            elif call.data == 'mater_u':
                await call.message.edit_reply_markup(reply_markup=in_mater_u)
            elif call.data == 'mater_e':
                await call.message.edit_reply_markup(reply_markup=in_mater_e)
            elif call.data == 'mater_d':
                await call.message.edit_reply_markup(reply_markup=in_mater_d)
            elif call.data == 'mater_f':
                await call.message.edit_reply_markup(reply_markup=in_mater_f)
            elif call.data == 'mater_n':
                await call.message.edit_reply_markup(reply_markup=in_mater_n)
        elif call.data == "pod_end":
            conversation_status[call.from_user.id] = 1
        elif call.data[1] == '_':
            sos[call.from_user.id] = call.data.split("_")[0]
            count = 1
            global callback_d
            callback_d = call.data
            message_counter[call.from_user.id] = 0
            message_counter[call.from_user.id] += count
            id_user = call.from_user.id
            for values in callback_parametr(call.data):
                tex, photo, movie, doc = values[1], values[2], values[3], values[4]
                await bot.send_message(id_user, text=tex)
                message_counter[call.from_user.id] += count
                if photo is not None:
                    await bot.send_message(id_user, text="А вот и фоточки: ")
                    message_counter[call.from_user.id] += count
                    for i in photo.split(', '):
                        await bot.send_photo(id_user, photo=i)
                        message_counter[call.from_user.id] += count
                if movie is not None:
                    await bot.send_message(id_user, text="И видео: ")
                    message_counter[call.from_user.id] += count
                    for i in movie.split(', '):
                        await bot.send_message(id_user, i)
                        message_counter[call.from_user.id] += count
                if doc is not None:
                    await bot.send_message(id_user, text="И документы: ")
                    message_counter[call.from_user.id] += count
                    for i in doc.split():
                        await bot.send_document(id_user, i)
                        message_counter[call.from_user.id] += count
                await bot.send_message(id_user, text='Продолжите', reply_markup=in_res)
                message_counter[call.from_user.id] += count
    except Exception:
        print("Проблемка")


while True:
    try:
        executor.start_polling(dispatcher=db, skip_updates=True)
    except (KeyboardInterrupt, SystemExit):
        break
    except Exception:
        logging.exception('polling error')
