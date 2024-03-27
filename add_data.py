from return_data_file import data_file


def add_row(new = True, row_to_data = [], data = [], nf = 1):
    if new:
        row_to_data.append(input("Введите свое имя: ") + ';')
        row_to_data.append(input("Введите свою фамилию: ") + ';')
        row_to_data.append(input("Введите дату рождения: ") + ';')
        row_to_data.append(input("Введите город: ") + "\n")
        data, nf = data_file()
    
    now_number_row = len(data) + 1
    row_to_data.insert(0, (str(now_number_row) + ';'))    
    with open(f'db/data_{nf}.txt', 'a', encoding='utf-8') as file:
        file.write("".join(row_to_data))
    print("Данные успешно записаны!")