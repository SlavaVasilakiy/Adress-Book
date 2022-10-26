def adding():
    to_add = []
    print("\nВы добавляете информацию в телефонную книгу.\n")
    to_add.append(input('Фамилия: '))
    to_add.append(input('Имя: '))
    to_add.append(input('Номер телефона: '))
    to_add.append(input('Описание: '))
    with open('last_key.txt', "r") as my_f:
        last_key = my_f.readline().split()
        new_key = int(last_key[-1])
    with open('Phonebook.csv', "a", encoding='utf-8') as base:
        base.write('\n{},{},{},{},{}'.format(new_key + 1, to_add[0], to_add[1], to_add[2], to_add[3]))
    with open('Phonebook.txt', "a", encoding='utf-8') as b_t:
        b_t.write(f'№ {new_key + 1}\nФамилия: {to_add[0]}\nИмя: {to_add[1]}\nНомер телефона: {to_add[2]}\nОписание: {to_add[3]}\n\n\n')
    with open('last_key.txt', "w", encoding='utf-8') as my_f:
        my_f.write(f"last_key = {new_key + 1}")
    return to_add