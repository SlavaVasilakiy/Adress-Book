from look import look
from print import print_csv, print_txt, print_all
from os import system


def input_contact_menu_choice():
    while True:
        print()
        print('-----------------------')
        print('Управление контактами')
        print('-----------------------')
        print()
        print('1. Показать все')
        print('2. Поиск записей')
        print('3. Добавить новую запись')
        print('4. Изменить существующую запись')
        print('5. Удалить запись')
        print('0. Выход')
        try:
            choice1 = int(input('Выберите пункт меню: '))
        except ValueError:
            print('Неверный пункт меню')
            # logg.error_enter()
            return input_contact_menu_choice()
        if choice1 == 1:
            print('1. вывод данных из файла Phonebook.csv в консоль')
            print('2. вывод данных из файла Phonebook.txt в консоль')
            print('3. запись данных из всех файлов в файл Phonebook_all.csv')
            print('0. Вернуться в главное меню')
            try:
                choice2 = int(input('Выберите пункт меню: '))
            except ValueError:
                print('Неверный пункт меню')
                # logg.error_enter()
                return()
            if choice2 == 1:
                return 1
            if choice2 == 2:
                return 2
            if choice2 == 3:
                return input_contact_menu_choice()
            else:
                return input_contact_menu_choice()
        elif choice1 == 2:
            print('1. Найти номер по фамилии')
            print('2. Найти номер по имени')
            print('3. Поиск по номеру телефона')
            print('0. Вернуться в главное меню')
            try:
                choice3 = int(input('Выберите пункт меню: '))
            except ValueError:
                print('Неверный пункт меню')
                # logg.error_enter()
                return()
            if choice3 == 1:
                return 1
            if choice3 == 2:
                return 2
            if choice3 == 3:
                return 3
            else:
                return input_contact_menu_choice()
        elif choice1 == 3:
            return 3
        elif choice1 == 4:
            return 4
        elif choice1 == 5:
            return 5
        elif choice1 == 0:
            return exit()
        else:
            return input_contact_menu_choice()


print(input_contact_menu_choice())
