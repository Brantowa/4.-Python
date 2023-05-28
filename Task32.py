# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
list = [random.randint(-100,100) for i in range(10)]
print(list)
max_num = int(input('Введите максимальное значение диапазона '))
min_num = int(input('Введите минимальное значение диапазона '))
list_index = []
count = 0

for i in list:
    if max_num>=i>=min_num:
        list_index.append (count)
    count=count+1
print(list_index)
