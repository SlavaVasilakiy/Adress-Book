# 2. Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
from file_writing import last_key

def data_entry():
    last_names = []
    names = []
    tels = []
    des = []
    while True:
        last_name = input("Введите фамилию или 'end' для окончания ввода: ")
        if last_name == 'end':
            break
        name = input("Введите имя: ")
        tel = input("Введите номер телефона: ")
        info = input("Введите комментарий: ")
        last_names.append(last_name)
        names.append(name)
        tels.append(tel)
        des.append(info)

    pb = {}
    key_start = last_key()
    for i in range(key_start - 1, len(last_names) + key_start):
        key = i + 1
        pb[key] = []
        pb[key].append(last_names[i])
        pb[key].append(names[i])
        pb[key].append(tels[i])
        pb[key].append(des[i])
        #key_start += i
    return pb
