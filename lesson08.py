# Задача №49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной
def menu():
    flag = True
    print("Выберете действие")
    print("1. Вывести все записи")
    print("2. Поиск записи")
    print("3. Добавить запись")
    print("4. Удалить запись")
    print("5. Изменить запись")
    print("0. Выход из программы")
    while flag:
        result_choice = input("Введите число [1-5, 0]: ")
        if result_choice.isnumeric():
            result_choice = int(result_choice)
            if result_choice in [1, 2, 3, 4, 5, 6, 0]:
                flag = False
            else:
                print("Ошибка ввода. Введите число из диапазона 1..5 или 0")
        else:
            print("Введено не число")
    return result_choice 
   
def read_data(_data):
    data = []
    with (open(_data, 'r', encoding="utf-8")) as _file:
        for line in _file:
            data.append(line.strip())
    return data

def save_contact(_data, _type_operation, _contact):
    with (open(_data, _type_operation, encoding="utf-8")) as _file:
        for line in _contact:
            _file.write(str(line)+"\n")
        
def add_contact(_data):  
    new_contact_last_name = input("Введите Фамилию: ")
    new_contact_first_name = input("Введите Имя: ")
    new_contact_surrender_name = input("Введите Отчество: ")
    new_contact_number = input("Введите Номер: ")
    input_string = new_contact_last_name + ';' + new_contact_first_name + ';' + new_contact_surrender_name + ';' + new_contact_number
    record = []
    record.append(input_string)
    save_contact(_data, 'a', _contact=record)

def search_contact(_data, search_name, position = 0):
    search_contact_data = []
    for contact in _data:
        record = contact.split(';')
        if  search_name.lower() == record[position].lower():
            search_contact_data.append(contact)
    return search_contact_data     

def delete_contact(_data):
    phonebook_data = read_data(_data)
    print_records(phonebook_data)
    print_divider(n = 10)
    print("")
    number_delete_record = input("Введите номер записи для удаления: ")
    print("Удаляем запись - " + phonebook_data.pop(int(number_delete_record) - 1 ))
    print_records(phonebook_data)
    save_contact(_data, 'w', _contact=phonebook_data)

def input_edit(_string, defult_value = ''):
    result = input(_string + f" [{defult_value}]: ")
    return result if len(result) > 0 else defult_value
    
def edit_contact(_data):
    phonebook_data = read_data(_data)
    print_records(phonebook_data)
    print_divider(n = 10)
    print("")
    number_delete_record = int(input("Введите номер записи для редактирования: ")) - 1
    edit_record = phonebook_data.pop(number_delete_record)
    print("Редактируем запись - " + edit_record)
    temp_list = edit_record.split(';')
    last_name = temp_list[0]
    first_name = temp_list[1]
    surrender_name = temp_list[2]
    phone_number = temp_list[3]
    last_name = input_edit("Введите Фамилию", last_name)
    first_name = input_edit("Введите Имя", first_name)
    surrender_name = input_edit("Введите Отчество", surrender_name)
    phone_number = input_edit("Введите Номер", phone_number)
    input_string = last_name + ';' + first_name + ';' + surrender_name + ';' + phone_number
    phonebook_data.insert(number_delete_record, input_string)
    save_contact(_data, 'w', _contact=phonebook_data)
        
def print_records(_data):
    counter = 1
    for contact in _data:
        print(str(counter), end=' | ')
        print(*contact.split(';'))
        counter += 1

def print_divider(n = 80):
    print('=' * n)    

def main():
    work_flag = True
    phonebook_data = read_data(data_file)
    while work_flag:
        user_choice = menu()
        print(f"Выбрано действие - {user_choice}")
        if user_choice == 1:
            print_records(phonebook_data)
        elif user_choice == 2:
            search = input("Введите фамилию: ")
            find_contact = search_contact(phonebook_data, search)
            if len(find_contact) > 0:
                print_records(find_contact)
            else:
                print("Запись не найдена")
        elif user_choice == 3:
            add_contact(data_file)
            phonebook_data = read_data(data_file)
        elif user_choice == 4:
            delete_contact(data_file)
            phonebook_data = read_data(data_file)
        elif user_choice == 5:
            edit_contact(data_file)
            phonebook_data = read_data(data_file)
        elif user_choice == 0:
            work_flag = False   
        print_divider()             
        
        
    
data_file = 'data\data.txt'
main()

