# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y



equation = 'y = -12x + 11111140.2121'
x = 2.5

coef = equation.split()
print(coef)
k_str = coef[2]
print(k_str)
k = int(k_str[:-1])
print(k)
b = float(coef[4])
print(b)
y = k*x + b
print(y)
