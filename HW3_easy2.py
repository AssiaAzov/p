# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

def max_count(a, b, c):
    return max(a, b, c)

num = tuple(map(int, input('Введите 3 числа через пробел: ').split()))
print(max_count(num[0], num[1], num[2]))
