# Вариант 15. Вывести все четные натуральные числа до n, крайняя левая цифра которых не превышает 5.
import math
print("Введите число n:",end='')
n = int(input())
N = n
a = []
for i in range(1, n+1):
    a.append(i)
print("Часть 1:")
print("----------------------")
print("Все четные натуральные числа до "+str(n), "крайняя левая цифра которых не превышает 5")
def fun(n):
    if n != 1:
        fun(n-1)
    if n % 2 == 0 and int(str(n)[0]) <= 5:
        print(n)
fun(n)
mini = 999999
print("Часть 2.1:")
print("----------------------")
print("Вывести все числа, сумма цифр которых меньше 6 ")
def fun(n):
    su = 0
    if n != 1:
        fun(n-1)
    if n % 2 == 0 and int(str(n)[0]) <= 5:
        for i in str(n):
            su += int(i)
        if su < 6:
            print(n)
fun(n)
print("Часть 2.2:")
print("----------------------")
print("Найдите минимальное число,длина факториала которого больше или равна половине N")
def fun(n):
    global mini
    if n != 1:
        fun(n-1)
    if n % 2 == 0 and int(str(n)[0]) <= 5 and len(str(math.factorial(n))) >= N//2:
        if mini > n:
            mini = n
fun(n)
print(mini, (", длина факториала ="),len(str(math.factorial(mini))))
