# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

def max_len(*strings):
   return max(strings, key=len)

my_strs = tuple(map(str, input('Введите строки через пробел: ').split()))
print(max_len(*my_strs))
