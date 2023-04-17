
# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, 
# т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

ticket = int(input('Введите 6-ти значный номер билета: '))

if (ticket%10) + ((ticket//10)%10) + ((ticket//100)%10) == (ticket//100000) + ((ticket//1000)%10) + ((ticket//10000)%10):
 print(ticket, '-> yes')
else: 
 print(ticket, '-> no')