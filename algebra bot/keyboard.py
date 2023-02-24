from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


in_start = InlineKeyboardMarkup(resize_keyboard=True)


in_start2 = InlineKeyboardButton('Материалы🔎', callback_data='mater')
in_start3 = InlineKeyboardButton('История математики📚', callback_data='histor')
in_start1 = InlineKeyboardButton('Написать админу💬', callback_data='podd')

in_start.add(in_start1)
in_start.add(in_start2)
in_start.add(in_start3)

###################################################################################

nazad = InlineKeyboardButton('⬅️Назад⬅️', callback_data='nazad1')
##################################################################################

ese = InlineKeyboardMarkup(resize_keyboard=True)

in_ese = InlineKeyboardButton('↘️Ещё задача↙️', callback_data='resume2')
ese.add(in_ese)

###################################################################################

in_res = InlineKeyboardMarkup(resize_keyboard=True)

in_resu2 = InlineKeyboardButton('↘️Практические задачи↙️', callback_data='resume2')
in_resu3 = InlineKeyboardButton('✖️Скрыть✖️', callback_data='resume3')
in_res.add(in_resu2)
in_res.add(in_resu3)


###################################################################################
pod_end = InlineKeyboardMarkup()
pod_en = InlineKeyboardButton('🛑Закончить🛑', callback_data='pod_end')
pod_end.add(pod_en)
pod_end.add(nazad)

####################################################################################

in_mater = InlineKeyboardMarkup(resize_keyboard=True)
in_mater1 = InlineKeyboardButton('Выражения и их преобразования', callback_data='mater_v')
in_mater2 = InlineKeyboardButton('Уравнения', callback_data='mater_u')
in_mater3 = InlineKeyboardButton('Неравенства', callback_data='mater_n')
in_mater4 = InlineKeyboardButton('Функции', callback_data='mater_f')
in_mater5 = InlineKeyboardButton('Действительные числа. Приближённые вычисления', callback_data='mater_d')
in_mater6 = InlineKeyboardButton('Элементы статистики', callback_data='mater_e')
in_mater.add(in_mater1)
in_mater.add(in_mater2)
in_mater.add(in_mater3)
in_mater.add(in_mater4)
in_mater.add(in_mater5)
in_mater.add(in_mater6)
in_mater.add(nazad)
##########################################################################################

##########################################################################################

in_histor = InlineKeyboardMarkup(resize_keyboard=True)
in_histor1 = InlineKeyboardButton('Учёные', callback_data='histor_u')
in_histor2 = InlineKeyboardButton('Интересные факты из жизни учёных', callback_data='histor_i')
in_histor3 = InlineKeyboardButton('Интересные факты математики', callback_data='histor_f')
in_histor4 = InlineKeyboardButton('Создание теорем', callback_data='histor_c')
in_histor.add(in_histor1)
in_histor.add(in_histor2)
in_histor.add(in_histor3)
in_histor.add(in_histor4)
in_histor.add(nazad)

############################################################################################

in_mater_v = InlineKeyboardMarkup(resize_keyboard=True)

in_mater_v1 = InlineKeyboardButton('Выражения', callback_data='v_1')
in_mater_v2 = InlineKeyboardButton('Тождество', callback_data='v_2')
in_mater_v3 = InlineKeyboardButton('Одночлены', callback_data='v_3')
in_mater_v4 = InlineKeyboardButton('Многочлены', callback_data='v_4')
in_mater_v5 = InlineKeyboardButton('Формулы сокращённого умножения', callback_data='v_5')
in_mater_v7 = InlineKeyboardButton('Рациональная дробь', callback_data='v_6')
in_mater_v8 = InlineKeyboardButton('Степень с целым показателем', callback_data='v_7')
in_mater_v9 = InlineKeyboardButton('Квадратный корень с целым показателем', callback_data='v_8')
nazad2 = InlineKeyboardButton('⬅️Назад⬅️', callback_data='nazad2')
in_mater_v.add(in_mater_v1)
in_mater_v.add(in_mater_v2)
in_mater_v.add(in_mater_v3)
in_mater_v.add(in_mater_v4)
in_mater_v.add(in_mater_v5)
in_mater_v.add(in_mater_v7)
in_mater_v.add(in_mater_v8)
in_mater_v.add(in_mater_v9)
in_mater_v.add(nazad2)

##########################################################################################

in_mater_u = InlineKeyboardMarkup(resize_keyboard=True)

in_mater_u1 = InlineKeyboardButton('Корень уравнения', callback_data='u_1')
in_mater_u2 = InlineKeyboardButton('Рациональные уравнения', callback_data='u_2')
in_mater_u3 = InlineKeyboardButton('Равносильные уравнения', callback_data='u_3')
in_mater_u4 = InlineKeyboardButton('Свойства уравнений', callback_data='u_4')
in_mater_u5 = InlineKeyboardButton('Линейные уравнения', callback_data='u_5')
in_mater_u6 = InlineKeyboardButton('Квадратные уравнения', callback_data='u_6')
in_mater_u7 = InlineKeyboardButton('Неполные квадратные уравнения', callback_data='u_7')
in_mater_u8 = InlineKeyboardButton('Дискриминант', callback_data='u_8')
in_mater_u9 = InlineKeyboardButton('Теорема Виета', callback_data='u_9')
in_mater_u10 = InlineKeyboardButton('Как решать дробные рациональные уравнения', callback_data='u_10')
in_mater_u11 = InlineKeyboardButton('Решение уравнений с двумя переменными', callback_data='u_11')
in_mater_u12 = InlineKeyboardButton('Решение системы уравнений', callback_data='u_12')
in_mater_u.add(in_mater_u1)
in_mater_u.add(in_mater_u2)
in_mater_u.add(in_mater_u3)
in_mater_u.add(in_mater_u4)
in_mater_u.add(in_mater_u5)
in_mater_u.add(in_mater_u6)
in_mater_u.add(in_mater_u7)
in_mater_u.add(in_mater_u8)
in_mater_u.add(in_mater_u9)
in_mater_u.add(in_mater_u10)
in_mater_u.add(in_mater_u11)
in_mater_u.add(in_mater_u12)
in_mater_u.add(nazad2)

##########################################################################################

in_mater_n = InlineKeyboardMarkup(resize_keyboard=True)

in_mater_n1 = InlineKeyboardButton('Строгие и нестрогие неравенства', callback_data='n_1')
in_mater_n2 = InlineKeyboardButton('Свойства нераваенств', callback_data='n_2')
in_mater_n3 = InlineKeyboardButton('Сложение и умножение неравенств', callback_data='n_3')
in_mater_n4 = InlineKeyboardButton('Решение неравенств', callback_data='n_4')
in_mater_n5 = InlineKeyboardButton('Равносильные неравенства', callback_data='n_5')
in_mater_n6 = InlineKeyboardButton('Числовой промежуток', callback_data='n_6')
in_mater_n7 = InlineKeyboardButton('Линейные неравенства', callback_data='n_7')
in_mater_n8 = InlineKeyboardButton('Система неравенств', callback_data='n_8')

in_mater_n.add(in_mater_n1)
in_mater_n.add(in_mater_n2)
in_mater_n.add(in_mater_n3)
in_mater_n.add(in_mater_n4)
in_mater_n.add(in_mater_n5)
in_mater_n.add(in_mater_n6)
in_mater_n.add(in_mater_n7)
in_mater_n.add(in_mater_n8)
in_mater_n.add(nazad2)

##########################################################################################

in_mater_f = InlineKeyboardMarkup(resize_keyboard=True)

in_mater_f1 = InlineKeyboardButton('Шоце за функция и этот график функции', callback_data='f_1')
in_mater_f2 = InlineKeyboardButton('Линейная функция и её график', callback_data='f_2')
in_mater_f3 = InlineKeyboardButton('Прямая пропорциональность', callback_data='f_3')
in_mater_f4 = InlineKeyboardButton('Обратная пропорциональность', callback_data='f_4')
in_mater_f5 = InlineKeyboardButton('Свойства функции', callback_data='f_5')
# Нужно дописать
in_mater_f.add(in_mater_f1)
in_mater_f.add(in_mater_f2)
in_mater_f.add(in_mater_f3)
in_mater_f.add(in_mater_f4)
in_mater_f.add(in_mater_f5)
in_mater_f.add(nazad2)

##########################################################################################

in_mater_d = InlineKeyboardMarkup(resize_keyboard=True)

in_mater_d1 = InlineKeyboardButton('Множество чисел', callback_data='d_1')
in_mater_d2 = InlineKeyboardButton('Рациональные числа', callback_data='d_2')
in_mater_d3 = InlineKeyboardButton('Стандартный вид числа', callback_data='d_3')
in_mater_d4 = InlineKeyboardButton('Абсолютная погрешность приближённого значения числа', callback_data='d_4')
in_mater_d5 = InlineKeyboardButton('Относительная погрешность приближённого значения числа', callback_data='d_5')
in_mater_d.add(in_mater_d1)
in_mater_d.add(in_mater_d2)
in_mater_d.add(in_mater_d3)
in_mater_d.add(in_mater_d4)
in_mater_d.add(in_mater_d5)
in_mater_d.add(nazad2)

##########################################################################################

in_mater_e = InlineKeyboardMarkup(resize_keyboard=True)

in_mater_e1 = InlineKeyboardButton('Статестичесские характеристики', callback_data='e_1')
in_mater_e2 = InlineKeyboardButton('Генеральная совокупность', callback_data='e_2')
in_mater_e3 = InlineKeyboardButton('Таблицы частот и относительных частот', callback_data='e_3')
in_mater_e4 = InlineKeyboardButton('Диаграммы, полигоны, гистограммы', callback_data='e_4')

in_mater_e.add(in_mater_e1)
in_mater_e.add(in_mater_e2)
in_mater_e.add(in_mater_e3)
in_mater_e.add(in_mater_e4)

in_mater_e.add(nazad2)
