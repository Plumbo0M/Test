from data_create import name_data, surname_data, phone_data, address_data
import os

def get_path(mpath: str) -> os.path:
    return os.path.join(os.getcwd(), mpath)


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()

    var = int(input(f"В каком формате Вы хотите записать данные?\n\n"
                    f"1 Вариант:\n\n"
                    f"{surname}\n"
                    f"{name}\n"
                    f"{phone}\n"
                    f"{address}\n\n"
                    f"2 Вариант:\n\n"
                    f"{surname};{name};{phone};{address}\n\n"
                    f"Выберите номер варианта: "))

    while var != 1 and var != 2:
        print('Попробуйте ещё раз выбрать правильную команду')
        var = int(input("Введите номер варианта: "))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name}\n{surname}\n{phone}\n{address}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{address}\n\n')


def print_data():
    print('Вывожу данные для Вас из 1-ого файла\n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data_first = file.readlines()
        data_first_version_second = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_version_second.append(''.join(data_first[j:i + 1]))
                j = i
        data_first = data_first_version_second
        print(''.join(data_first))
        # print(*data_first, sep='')

    print('Вывожу данные для Вас из 2-ого файла\n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data_second = list(file.readlines())
        print(*data_second)
    return data_first, data_second


def put_data():
    print('Из какого файла Вы хотите изменить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:
        file_name = 'data_first_variant.csv'
    else:
        file_name = 'data_second_variant.csv'

    print(f"Какую именно запись по счету Вы хотите изменить в файле {file_name}?")
    number_journal = int(input('Введите номер записи: '))

    with open(file_name, 'r') as file:
        lines = file.readlines()

    if 0 < number_journal <= len(lines):
        print(f'Текущее значение записи {number_journal}: {lines[number_journal-1].strip()}')
        new_value = input('Введите новое значение для записи: ')
        lines[number_journal - 1] = f'{new_value}\n'

        with open(file_name, 'w') as file:
            file.writelines(lines)

        print(f'Запись изменена: {new_value}')
    else:
        print('Некорректный номер записи.')


def delete_data():
    print('Из какого файла Вы хотите удалить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:
        file_name = 'data_first_variant.csv'
    else:
        file_name = 'data_second_variant.csv'

    print(f"Какую именно запись по счету Вы хотите удалить в файле {file_name}?")
    number_journal = int(input('Введите номер записи: '))

    with open(file_name, 'r') as file:
        lines = file.readlines()

    if 0 < number_journal <= len(lines):
        deleted_line = lines.pop(number_journal - 1)

        with open(file_name, 'w') as file:
            file.writelines(lines)

        print(f'Запись удалена: {deleted_line}')
    else:
        print('Некорректный номер записи.')
