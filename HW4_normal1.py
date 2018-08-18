# Задача - 1
# Запросите у пользователя имя, фамилию, email. Теперь необходимо совершить проверки, имя и фамилия должны иметь заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре, допускается нижнее подчеркивание и цифры, потом @, потом текст, допускаются цифры, точка, ru или org или com.
# Например:
# Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email (спецсимвол, заглавная буква, .net), te_4_st@test.com - верно указан.


pattern_name = '[A-ZА-Я][a-zа-я]+$'
pattern_email = '[a-z_0-9]+@[a-z0-9]+\.(ru|com|org)$'

import re

def check(str, pattern):
    result = re.match(pattern, str)
    while not result:
        str = input('Ошибка ввода! Попробуйте еще раз: ')
        result = re.match(pattern, str)
    else:
        print('Ok')


name = input('Введите Ваше имя: ')
check(name, pattern_name)

surname = input('Введите Вашу фамилию: ')
check(surname, pattern_name)

email = input('Введите адрес электронной почты: ')
check(email, pattern_email)


