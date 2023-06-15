# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!

# def switch_it_up(number):
#     pass


number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
switch = ['one', 'two', 'three', 'four', 'five', 'six', 'seven','eight', 'nine']

n = int(input('Введите цифру от 1 до 9 - '))

def switch_it_up(number):

    if 1 <= n <= 9:

        for i in number:  
            i = switch[n - 1]
            
            return i
          
    elif 10 <= n <= 0:

        print('None')
     

i = switch_it_up(number)

print (f'Число {n} - {i}')
    



