# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

# def remove_exclamation_marks(s):
#     pass

#Способ №1
# import re

# s = 'Hi! My name is Mary! I am studying Phyton!'
# s = re.sub(r'\W', '', s)
# print(s)



#Способ №2


s = input('Введите текст - ')

def remove_exclamation_marks(s):
    marks = '!'
    for i in marks:
        s = s.replace(i, '')
    return s
s = remove_exclamation_marks(s)
print (s)





