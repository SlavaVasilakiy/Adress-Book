

def input_contact_menu_choice():
    while True:
        print()
        print('-----------------------')
        print('Управление контактами')
        print('-----------------------')
        print()
        print('1. Показать все')
        print('2. Найти номер по фамилии')
        print('3. Найти номер по имени')
        print('4. Поиск по номеру телефона')
        print('5. Добавить новую запись')
        print('6. Изменить существующую запись')
        print('7. Удалить запись')
        print('0. Выход')
        try:
            choice = int(input('Выберите номер операции: '))
        except ValueError:
            print('Неверный пункт меню')
            # logg.error_enter()
            return input_contact_menu_choice()
        if choice == 1:
            return 1
        elif choice == 2:
            return 2
        elif choice == 3:
            return 3
        elif choice == 4:
            return 4
        elif choice == 5:
            return 5
        elif choice == 6:
            return 6
        elif choice == 7:
            return 7
        elif choice == 0:
            return exit()
        else:
            print('\nНеверный пункт меню !!!')
            # logg.error_enter()
            return input_contact_menu_choice()


print(input_contact_menu_choice())
