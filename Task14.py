# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
n = int(input('Ведите число N: '))
sq = 0
count = 0
while sq < n:
    sq = 2**count
    if sq <= n:
        print (sq)
    count = count + 1
