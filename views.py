
def view(phonebook):
    '''Функция представления пользователю данных.
    Принимает в виде аргумента список и через цикл выводит его в консоль.'''
    for data in phonebook:
        print('Информация о контакте:', data[0], end='\n')
        print('Фамилия:', data[1])
        print('Имя:', data[2])
        print('Отчество:', data[3])
        print('Организация:', data[4])
        print('Рабочий телефон:', data[5])
        print('Личный телефон:', data[6])
        print()


