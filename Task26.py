# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# def deg (x,y):
#     res = 1
#     for y in range(1,y+1):
#         res *=x 
#     return res

# print(deg(5,3))
    
def deg (x, y):
    if y == 0:
        return 1
    if y == 1:
        return x
    return x * deg(x, y-1)

A = int(input('Введите число: '))
B = int(input('Введите степень: '))
print(A, 'в степени', B, 'равно', deg(A,B))
