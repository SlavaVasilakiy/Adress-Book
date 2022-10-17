#2. Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
from pprint import pprint

def last_names():
    last_names = []
    while True:
        last_name = input("Введите фамилию: ")
        if last_name == 'end':
            return last_names
        last_names.append(last_name)

def get_name():
    names = []
    while True:
        name = input("Введите имя: ")
        if name == 'end':
            return names
        names.append(name)

def telephone():
    tels = []
    while True:
        tel = input("Введите номер телефона: ")
        if tel == 'end':
            return tels
        tels.append(tel)

def info():
    des = []
    while True:
        info = input("Введите комментарий: ")
        if info == 'end':
            return des
        des.append(info)


def dic(last_names, names, tels, info):
    pb={}
    for i in range(1, len(last_names)+1):
        key=i
        pb[key]=[]
        pb[key].append(last_names[i-1])
        pb[key].append(names[i-1])
        pb[key].append(tels[i-1])
        pb[key].append(info[i-1])
    return pb
