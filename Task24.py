number = int(input('Введите общее количество элементов в списке '))
first_list = list()
for i in range(number):
    element = int(input('Введите элементы списка '))
    first_list.append(element)
print (first_list)

count_list = list()
for i in range(len(first_list)-1):
    count_list.append(first_list[i-1] + first_list[i] + first_list[i+1])
count_list.append(first_list[-2] + first_list[-1] + first_list[0])
print(max(count_list))
    