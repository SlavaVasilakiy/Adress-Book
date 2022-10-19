from os import path


def print_csv(): # печать в консоль из файла Phonebook.csv
    file = 'Phonebook.csv'
    if path.exists(file):
        with open(file, 'r', encoding='utf-8') as text:
            text_csv = text.readlines()
            for i, v in enumerate(text_csv):
                print(v.strip())

def print_txt(): # печать в консоль из файла Phonebook.txt
    file = 'Phonebook.txt'
    if path.exists(file):
        with open(file, 'r', encoding='utf-8') as text:
            text_txt = text.readlines()
            for i, v in enumerate(text_txt):
                print(v.strip())

def print_all():  # запись данных из всех файлов в отдельный фаил Phonebook_all.csv
    file = 'Phonebook_all.csv'
    file_csv = 'Phonebook.csv'
    file_txt = 'Phonebook.txt'
    with open(file, 'w', encoding='utf-8') as text:
        if path.exists(file_csv) and path.exists(file_txt):
            with open(file_csv, 'r', encoding='utf-8') as text_csv,\
                open(file_txt, 'r', encoding='utf-8') as text_txt:
                t_csv = text_csv.readlines()
                text.write(f'Данные из телефонного справочника в фаиле Phonebook.csv!\n\n')
                for i, v in enumerate(t_csv):
                    text.write(f'{v.strip()}\n')
                t_txt = text_txt.readlines()
                text.write(f'\nДанные из телефонного справочника в фаиле Phonebook.txt!\n\n')
                for i, v in enumerate(t_txt):
                    text.write(f'{v.strip()}\n')
                print('Все данные успешно занесены в фаил Phonebook_all.csv')