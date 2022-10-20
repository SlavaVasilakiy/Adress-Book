from log import error_enter


def user_choice():
    try:
        choice1 = int(input('Выберите пункт меню: '))
    except ValueError:
        print('Ошибка ввода')
        error_enter()
    return choice1

def data_search():
    try:
        search = input('Введите данные  для поска контакта: ')
    except ValueError:
        print('Ошибка ввода')
        error_enter()
    return search