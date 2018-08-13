# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3
kv = int(input('Введите номер квартиры: '))

#строим башню)
tower = []
i = 1
while i <= 20:
    tower.append(i)
    i += 1
print(tower)
e = 1
b = 0
c = 1
n = 1
k = 1
i = 0
n_fl = 1
for j in range (4):
    i += 1
    for floor in tower[b:e]:
        floor = []
        for _ in range(i):
            floor.append(n)
            n += 1
        print(floor)
        if kv in floor:
            n_kv = floor.index(kv)+1
            print('N квартиры слева:', n_kv, ',', 'N этажа:', n_fl)
        n_fl += 1

    k += 1
    b = e + 1
    e = b + k










