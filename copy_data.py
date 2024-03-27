# модуль для копирования/переноса контакта из одной БД в другую БД

from return_data_file import data_file
from add_data import add_row 
from delete_data import delete_row


def copy_contact():
    data1, nf1 = data_file()
    count_rows = len(data1)
    number_row = int(input(f"Введите номер строки для копирования "
                           f"от 1 до {count_rows}: "))
    while number_row < 1 or number_row > count_rows:
        number_row = int(input(f"Ошибка!"
                               f"Введите номер строки "
                               f"от 1 до {count_rows}: "))
    print("Необходимо выбрать файл куда будет осуществляться копирование.\n")
    data2, nf2 = data_file()
    if nf1 == nf2:
        print("Контакт и так уже в этом файле.")
    else:
        method_copy = int(input("Какой метод копирования контакта вы хотите использовать:\n"
                    "1. Перенос\n"
                    "2. Копирование\n"
                    "Выберит режим, с которым Вы хотите работать\n"
                       "Введите цифру 1 или 2: "))
        while method_copy < 1 or method_copy > 2:
            method_copy = int(input("Ошибка!!!\n"
                            "Введите цифру 1 или 2: "))
        row_to_data = data1[number_row-1]
        add_row(False, list(row_to_data[2:]), data2, nf2)
        if method_copy == 1:
            delete_row(False, data1, nf1, number_row)


    
    # data[number_row - 1] = f'{number_row};{name};{surname};{birthdate};{town}\n'
    # with open(f'db/data_{nf}.txt', 'w', encoding='utf-8') as file:
    #     file.writelines(data)
    # print("Данные успешно изменены!")