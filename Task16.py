# Требуется вычислить, сколько раз встречается число X в массиве. 
# Пользователь вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

N = int (input('Введите натуральное число - количество элементов  в массиве '))
list = []
for i in range(N):
    list.append (int(input('Введите элемент массива ')))
print(list)
X = int(input('Введите интересующее чило '))
print('Запрашиваемое число встречается', list.count(X), 'раз(а) в массиве')