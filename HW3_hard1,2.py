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


with open('player.txt','w+', encoding='utf-8') as file:
    line = str(player) + '\n'
    file.write(line)

with open('enemy.txt','w+', encoding='utf-8') as file:
    line = str(enemy) + '\n'
    file.write(line)


with open('player.txt', encoding='utf-8') as f:
    line = f.readline()
    dict_player = eval(line)


with open('enemy.txt', encoding='utf-8') as f:
    line = f.readline()
    dict_enemy = eval(line)


while dict_player['health'] > 0 and dict_enemy['health'] > 0:
    attack(dict_player, dict_enemy)
    print(dict_player['health'],dict_enemy['health'])
    if dict_enemy['health'] <= 0:
        print('Победил: ', dict_player['name'], 'Осталось ед. жизни: ', dict_player['health'])
        break
    else:
        attack(dict_enemy, dict_player)
        print(dict_player['health'], dict_enemy['health'])
else:
    if dict_player['health'] > 0:
        print('Победил: ', dict_player['name'], 'Осталось ед. жизни: ', dict_player['health'] )
    else:
        print('Победил: ', dict_enemy['name'], 'Осталось ед. жизни: ', dict_enemy['health'])
