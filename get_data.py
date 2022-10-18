# 2. Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.

def last_names():
    last_names = []
    names = []
    tels = []
    des = []
    while True:
        last_name = input("Введите фамилию: ")
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
    for i in range(len(last_names)):
        key = i + 1
        pb[key] = []
        pb[key].append(last_names[i])
        pb[key].append(names[i])
        pb[key].append(tels[i])
        pb[key].append(des[i])
    return pb


print(last_names())
