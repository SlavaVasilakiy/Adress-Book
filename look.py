from os import path


def look(search):   # поиск по данным
    # search = input('Введите данные  для поска контакта: ')
    file = 'Phonebook.csv'
    if path.exists(file):
        with open (file, 'r', encoding = 'utf-8') as text:
            count = False
            text_csv = text.readlines()
            for i, v in enumerate(text_csv):
                if search in v:
                    print('Данные из телефонного справочника в фаиле Phonebook.csv')
                    print(v.strip())
                    count = True
            if not count: print('Таких данных нет в справочнике фаила Phonebook.csv')

    file = 'Phonebook.txt'
    if path.exists(file):
        with open (file, 'r', encoding = 'utf-8') as text:
            count = False
            text_txt = text.readlines()
            for i, v in enumerate(text_txt):
                if search in v:
                    print('Данные из телефонного справочника в фаиле Phonebook.txt')
                    print(f'{text_txt[i]}{text_txt[i+1]}{text_txt[i+2]}{text_txt[i+3]}' )
                    count = True
            if not count: print('Таких данных нет в справочнике фаила Phonebook.txt')