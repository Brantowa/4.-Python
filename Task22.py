# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств

list_1 = [int(i) for i in input('Введите набор чисел через пробел в первый список ').split()]
set_1 = set(list_1)
print(set_1)
list_2 = [int(i) for i in input('Введите набор чисел через пробел во второй список ').split()]
set_2 = set(list_2)
print(set_2)

intersections_of_sets = set_1.intersection(set_2)

intersections_of_sets = list(intersections_of_sets)
sorted(intersections_of_sets)

print(intersections_of_sets)