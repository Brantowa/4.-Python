# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

N = int (input('Введите натуральное число - количество элементов в массиве '))
list = []
for i in range(N):
    list.append (int(input('Введите элемент массива ')))
print(list)
X = int(input('Введите интересующее чиcло '))

min_difference = abs(X - list[0])
the_closest = list[0]

for i in list:
    exam = abs(X - i)
    if exam <= min_difference:
       min_difference = exam
       the_closest = i

print('Cамый близкий по величине элемент к заданному числу -', the_closest)