# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, persoтn2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.

# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

player = {'name':input('Введите ваше имя: '), 'health': 100, 'damage': 85, 'armor': 1.2}
enemy = {'name':'Troll', 'health': 150, 'damage': 20, 'armor': 3}

def hit(napad, jertva):
    hit = napad['damage']/jertva['armor']
    return hit

def attack(napad, jertva):
    jertva['health'] = jertva['health'] - hit(napad, jertva)
    return jertva['health']

def write_in_file(file, dict):
    with open(file, 'w+', encoding='utf-8') as file:
        line = str(dict) + '\n'
        file.write(line)

def read_file(file, dict_pers):
    with open(file, encoding='utf-8') as f:
        line = f.readline()
        dict_pers = eval(line)
        print(dict_pers)

def read_file(file):
    with open(file, encoding='utf-8') as f:
        line = f.readline()
        return eval(line)

def print_win(dict_pers):
    print('Победил: ', dict_pers['name'], 'Осталось ед. жизни: ', dict_pers['health'])



write_in_file('player.txt', player)
write_in_file('enemy.txt', enemy)

dict_player = read_file('player.txt')
dict_enemy = read_file('enemy.txt')

while dict_player['health'] > 0 and dict_enemy['health'] > 0:
    attack(dict_player, dict_enemy)
    if dict_enemy['health'] <= 0:
        print_win(dict_player)
        break
    else:
        attack(dict_enemy, dict_player)
else:
    if dict_player['health'] > 0:
        print_win(dict_player)
    else:
        print_win(dict_enemy)
