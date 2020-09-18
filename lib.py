from tkinter import *

"""
    Необходимо создать программу для отметĸи стран, ĸоторые посетили 2 друга.
    Изначально стран у ĸаждого друга не введено. Пользователь вводит поочередно 
    или вразнобой посещенные страны для друзей. Страны в перечне ĸаждого друга 
    не должны повторяться (Пример: если друг1 посетил Испанию, Италию, Испанию 
    и Грецию, то посещенные страны друга1 будут выглядеть ĸаĸ Испания, Италия, Греция)
    Введенные страны без запроса на эĸране не выводятся. По требованию * вывести 
    на эĸран пунĸтов задания:
    - Общие посещенные страны (без повторений)
    - Страны, в ĸоторых побывал тольĸо один из друзей.
    - Весь списоĸ стран посещенных друзьями (без повторений) 
    
    Нужно использовать множества и их методы в решении.
"""
# -> создание окна и его параметры
root = Tk()
root.geometry('500x500+200+200')
root.title('Посещения стран')
root.config(bg='MediumAquamarine')

# -> виджеты окна
title_label = Label(root)
friend_1_label = Label(root)  # -> текст предшествующий вводу для первого друга
friend_2_label = Label(root)  # -> текст предшествующий вводу для второго друга
friend_1_entry = Entry(root)  # -> поле ввода данных для первого друга
friend_2_entry = Entry(root)  # -> поле ввода данных для второго друга
result_label = Label(root)  # -> отображает результат

button_confirm_f1 = Button(root)  # -> подтверждение ввода для первого друга
button_confirm_f2 = Button(root)  # -> подтверждение ввода для второго друга
button_result = Button(root)  # -> вызывает результат

# -> переменные типа str для хранения данных из entry
input_country_f1 = ''  # -> данные из entry первого друга (friend_1_entry)
input_country_f2 = ''  # -> данные из entry второго друга (friend_2_entry)


# -> параметры виджетов
def widgets_config():
    title_label.config(bg='MediumAquamarine', fg='CadetBlue', font=('Comic Sans Ms', 15), text='Посещения стран',
                       width=25)
    title_label.place(x=100, y=10)

    friend_1_label.config(text='Введите страну(-ы) для первого друга:', width=35, bg='MediumAquamarine', font='Arial 9')
    friend_1_label.place(x=10, y=60)

    friend_2_label.config(text='Введите страну(-ы) для второго друга:', width=35, bg='MediumAquamarine', font='Arial 9')
    friend_2_label.place(x=10, y=130)

    friend_1_entry.config(width=35, bd=3, relief=RIDGE)
    friend_1_entry.place(x=250, y=60)

    friend_2_entry.config(width=35, bd=3, relief=RIDGE)
    friend_2_entry.place(x=250, y=130)

    button_confirm_f1.config(width=12, text='Подтвердить', command=country_friend_1, font='Arial 9', bg='CadetBlue',
                             fg='white')
    button_confirm_f1.place(x=372, y=90)

    button_confirm_f2.config(width=12, text='Подтвердить', command=country_friend_2, font='Arial 9', bg='CadetBlue',
                             fg='white')
    button_confirm_f2.place(x=372, y=160)

    button_result.config(text='Вывести результаты посещения друзьями стран', width=60, command=result_country,
                         font='Arial 9', bg='CadetBlue', fg='white')
    button_result.place(x=35, y=200)

    result_label.config(bg='Aquamarine', width=60, height=15)
    result_label.place(x=35, y=235)


# -> получает данные из entry для первого друга
def country_friend_1() -> str:
    global input_country_f1
    if not input_country_f1:  # -> если переменная пустая
        # -> присваивает переменной строку из entry в нижнем регистре, удаляет пробелы по краям и заменяет , на пробел
        input_country_f1 = friend_1_entry.get().replace(',', ' ').strip().lower()
    else:
        new_input = friend_1_entry.get().replace(',', ' ').strip().lower()  # -> получает новый ввод из entry
        input_country_f1 = input_country_f1 + ' ' + new_input  # -> конкатенирует с уже существующими данными
    friend_1_entry.delete(0, END)  # -> очищает entry
    return input_country_f1


# -> получает данные из entry для второго друга
def country_friend_2() -> str:
    global input_country_f2
    if not input_country_f2:  # -> если переменная пустая
        # -> присваивает переменной строку из entry в нижнем регистре, удаляет пробелы по краям и заменяет , на пробел
        input_country_f2 = friend_2_entry.get().replace(',', ' ').strip().lower()
    else:
        new_input = friend_2_entry.get().replace(',', ' ').strip().lower()  # -> получает новый ввод из entry
        input_country_f2 = input_country_f2 + ' ' + new_input  # -> конкатенирует с уже существующими данными
    friend_2_entry.delete(0, END)  # -> очищает entry
    return input_country_f2


# -> находит общие страны, полный список стран и посещённые только одним из друзей. Выводит результат в label
def result_country():
    # -> сохраняет в переменную (type: set) одинаковые данные из двух entry (общие посещенные страны)
    general_countries = set.intersection(set(input_country_f1.split()), set(input_country_f2.split()))

    # -> сохраняет в переменную (type: set) уникальные элементы из двух entry (где побывал тольĸо один из друзей)
    visited_by_one_friend = set.symmetric_difference(set(input_country_f1.split()), set(input_country_f2.split()))

    # -> сохраняет в переменную (type: set) все элементы из двух entry (весь списоĸ стран посещенных друзьями)
    all_countries = set.union(set(input_country_f1.split()), set(input_country_f2.split()))

    # -> конверт.в str и переводит в верхний регистр первую букву каждого элемента
    general_countries_str = ', '.join(list(general_countries)).title()
    visited_by_one_friend_str = ', '.join(list(visited_by_one_friend)).title()
    all_countries_str = ', '.join(list(all_countries)).title()

    # -> устанавливает параметры для вывода результата в label
    result_label.config(text=f'- Общие посещенные страны:\n{general_countries_str}\n\n'
                             f'- Страны, в ĸоторых побывал тольĸо один из друзей:\n{visited_by_one_friend_str}\n\n'
                             f'- Весь списоĸ стран посещенных друзьями:\n{all_countries_str}', wraplength=370,
                        justify=LEFT, font='Arial 10', width=53)

# Ukraine canada Estonia usa Italy spain China hungary Japan - для проверки
