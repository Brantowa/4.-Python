# Заполните массив элементами арифметической прогрессии. Её первый элемент, 
# разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


first_item = int (input('Введите первый элемент массива '))
list = [first_item]
difference = int (input('Введите разницу '))
logitude = int (input('Введите длину '))
for i in range(logitude-1):
    list.append (list[i]+difference)
print(list)
