

def counter_lines():
    """Счетчик существующих записей в БД"""
    with open('db.TXT', mode='r', encoding='utf-8') as db:
        count = 0
        try:
            for line in db.readlines():
                count += 1
            return count

        except:
            return count


def phone_check():
    """Проверка корректности номера телефона.
    Принимает от пользователя строку и проверяет, состоит ли строка только из цифр
    и является ли ее длинна корректной для номера телефона"""
    flag = False
    while flag == False:
        phone = input('Введите номер: +7')
        if phone.isdigit():  # проверка содержимого строки
            if len(str(phone)) == 10:  # проверка длины строки
                flag = True
            else:
                print('Номер должен содержать 10 символов.')
        else:
            print('Телефон должен содержать только цифры.')

    return '+7' + phone
