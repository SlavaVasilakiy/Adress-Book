from os import path
from exceptions import data_search, key_choice



def look():  # поиск по данным
    search = data_search()
    file = 'Phonebook.csv'
    if path.exists(file):
        with open(file, 'r', encoding='utf-8') as text:
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
        with open(file, 'r', encoding='utf-8') as text:
            count = False
            text_txt = text.readlines()
            for i, v in enumerate(text_txt):
                if search in v:
                    while i == '':
                        i -= 1
                    print('Данные из телефонного справочника в фаиле Phonebook.txt')
                    print(f'{text_txt[i - 1]}{text_txt[i]}{text_txt[i + 1]}{text_txt[i + 2]}{text_txt[i + 3]}\n')
                    count = True
            if not count: print('Таких данных нет в справочнике фаила Phonebook.txt')
            return search


def delete_contact():
    name = look()
    print('Введите номер записи, которую хотите удалить:')
    del_key = str(key_choice())
    del_contact = f'№ {del_key}'
    with open('Phonebook.csv', 'r', encoding='utf-8') as data:
        contact = data.readlines()
        with open('Phonebook.csv', 'w', encoding='utf-8') as data:
            for i in range(len(contact)):
                if del_key and name not in contact[i]:
                    data.write(contact[i])
    
    with open('Phonebook.txt', 'r', encoding='utf-8') as data:
        contact = data.readlines()
        del_indexes=[]
        for i in range(len(contact)):
            if del_contact in contact[i]:
                del_indexes = [i,i+1,i+2,i+3,i+4]
                break
        with open('Phonebook.txt', 'w', encoding='utf-8') as data:
            for i in range(len(contact)):
                if i not in del_indexes:
                    data.write(contact[i])
    return del_key

def change_contact():
    name = look()
    print('Введите номер записи, которую хотите изменить: ')
    change_key = str(key_choice())
    change_contact = f'№ {change_key}'
    change_pos = input('Какой пункт вы хотите изменить? ')
    new_data = input('Введите новые данные:  ')
    with open('Phonebook.txt', 'r', encoding='utf-8') as data:
        contact = data.readlines()
        with open('Phonebook.txt', 'w', encoding='utf-8') as data:
            for i in range(len(contact)):
                if change_contact in contact[i]:
                    if change_pos=='Фамилия':
                        contact[i+1] = f'Фамилия: {new_data}\n'
                    elif change_pos=='Имя':
                        contact[i+2] = f'Имя: {new_data}\n'
                    elif change_pos=='Номер телефона':
                        contact[i+3] = f'Номер телефона: {new_data}\n'
                    elif change_pos=='Описание':
                        contact[i+4] = f'Описание: {new_data}\n'               
                data.write(contact[i])
                
    with open('Phonebook.csv', 'r', encoding='utf-8') as data:
        contact = data.readlines()
        with open('Phonebook.csv', 'w', encoding='utf-8') as data:
            for i in range(len(contact)):
                if f'{change_key},{name}' in contact[i]:
                    new_contact = contact[i].split(',')
                    if change_pos=='Фамилия':
                        new_contact[1] = new_data
                    elif change_pos=='Имя':
                        new_contact[2] = new_data
                    elif change_pos=='Номер телефона':
                        new_contact[3] = new_data
                    elif change_pos=='Описание':
                        new_contact[4] = f'{new_data}\n'
                    contact[i] = ','.join(new_contact)         
                data.write(contact[i])
    return change_key            

               
    



                
                  
