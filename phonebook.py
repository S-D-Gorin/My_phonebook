from check import counter_lines, phone_check
from views import view



def main():
    """Главная функция, выполняет проверку на наличие записей в БД,
    если записи есть, то запускает функцию выбора дальнейших действий,
    если записей нет, то предлагает пользователю создать первую запись"""

    if read_notes():  # проверка наличия записей
        choice_option()  # выбор дальнейших действий
    else:
        print('Записей пока нет.')
        print()
        print('Добавить новую запись?')

        flag = False
        while not flag:  # бесконечный цикл для выбора ответа на предложение создания новой записи
            coice = input('Y/N:').upper()  # переменная хранящая выбор пользователя
            if coice == 'Y':
                add_note()  # запуск функции создающей новую запись
                flag = True
            elif coice == 'N':
                print('Нет так нет.')
                flag = True
            else:
                print('Не та кнопка.')


def all_notes():
    """Функция обращается к БД через функцию чтения и передает все данные в функцию представления"""
    print('Все записи справочника:')
    print()
    view(read_notes())


def read_notes():
    """Функция считывающая данные из БД. Передает в return список,
    где каждая запись представлена отдельно, во вложенном списке."""

    with open('db.TXT', mode='r', encoding='utf-8') as db:
        phonebook = []  # переменная для хранения вложеных списков
        for line in db.readlines():  # каждая итерация цикла создает запись из БД во вложенном списке
            phonebook.append(line.split())
        # print(phonebook)
        return phonebook

def write_notes(data, mode):
    """Функция записи даных в БД. В аргументах передается:
    1. data - что нужно записать
    2. mode - метод записи: "W" для перезаписи всего файла или "A" для его дополнения"""

    with open('db.TXT', mode=mode, encoding='utf-8') as db:
        db.write(data)


def edit():
    """Функция редактирования существующих записей.
    Принимает от пользователя номер записи и выполняет проверку:
    если введенное число больше, чем количество записей в БД то
    выводится сообщение, что такой записи нет.

    Принцип работы: Все записи сохраняются в список, где каждая запись представляет отдельный, вложеный список.
    Далее, по индексу изменяются данные в выбранном вложенном списке и весь массив загружается обратно в БД"""

    id = int(input("Введите номер записи: "))  # ввод номера записи

    if id > counter_lines():  # сравнение введенных данных и количества записей в БД
        print('Такая запись не найдена!')
    else:
        print(f'Редактирование записи № {id}')

        my_notes = read_notes()  # переменная хранит в себе все записи из БД
        my_notes[id-1] = form_new_note().split()  # редактирование элемента списка с индексом, который ввел пользователь
        my_notes[id-1][0] = id  # присвоение номера записи

        write_notes('', 'w')  # очистка БД для дальнейшей записи отредактированных данных

        for line in my_notes:  # каждая итерация цикла возвращает записи в БД
            note = ''
            for element in line:  # вложенный цикл формирует строки для записи
                note += str(element)  # элемент строки
                note += ' '  # разделитель между элементами

            note += '\n'  # В конце каждой записи добавляется оператор переноса на следующую стоку
            write_notes(note, 'a')  # В функцию записи передается строка и методо записи т.е. добавления


def form_new_note():
    """Функция-шаблон для добавления новых записей"""

    id = counter_lines() + 1  # счетчик строк в БД для присвоения ID записи
    filname = input('Фамилия: ').title()
    name = input('Имя: ').title()
    faname = input('Отчество: ').title()
    organization = input('Место работы: ').title()
    print('Телефон рабочий: ')
    work_tel = phone_check()  # проверка корректности введенного номера телефона
    print('Телефон мобильный: ')
    personal_tel = phone_check()  # проверка корректности введенного номера телефона

    # строка сформированная для записи в БД
    return f'{id} {filname} {name} {faname} {organization} {work_tel} {personal_tel}\n'


def add_note():
    """Добавление записи."""
    write_notes(form_new_note(), 'a')   # вызов функции для записи данных в БД
                                        # первый аргумент - функция шаблонизатор вносимых данных
                                        # второй аргумент - метод записи БД т.е. добавление


def search():
    """Поиск по всем значениям в БД.
    Принимает от пользователя строку и ищет соответствия по всем элементам в БД"""
    find_to = input('Поиск: ')
    print()
    if find_to.isalpha():  # провера типа содержимого строки
        find_to = find_to.title()  # если строка состоит из букв, то первый символ переводится в верхний регистр

    flag = False  # флаг для отчета о результатах поиска

    for line in read_notes():  # цикл берет построчно все записи из БД
        for el in line[1:]:  # вложеный цикл сравнивает элементы строки с введеным в поиск словом без учета ID
            if find_to in el:  # если есть соответствие
                view([line]) # то выводится вся строка через функцию представления
                flag = True

    if flag:
        print('Это все, что удалось найти.')
    else:
        print('Запись не найдена')


def choice_option():
    """Функция предлагающая пользователю выбор возможных операций"""
    flag = False

    while flag == False:  # бесконечный цикл для выбора операции

        print("W - добавить запись.")
        print("A - просмотр всех записей.")
        print("S - поиск.")
        print("D - редактирование записи.")

        choice = input('Выберите действие: ').lower()
        print()

        if choice == 'a':
            all_notes()
            flag = True
        elif choice == 'w':
            add_note()
            flag = True
        elif choice == 's':
            search()
            flag = True

        elif choice == 'd':
            edit()
            flag = True

        else:
            print()
            print('Не та кнопка.')


if __name__ == '__main__':
    print("My phonebook @sdg9999")
    main()
