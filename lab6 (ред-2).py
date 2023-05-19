# Вариант 15. Вывести все четные натуральные числа до n, крайняя левая цифра которых не превышает 5.
import math

n = int(input('Введите число n:'))
su = 0
N=n
print("Часть 1:")
print("----------------------")
print("Все четные натуральные числа до", n, "крайняя левая цифра которых не превышает 5")


def fun(n):
    for i in range(2, n + 1, 2):
        if int(str(i)[0]) <= 5:
            print(i)


fun(n)
mini = 999999
print("Часть 2.1:")
print("----------------------")
print("Вывести все числа, сумма элементов которых меньше 6 ")


def fun(n):
    su = 0
    for i in range(2, n + 1, 2):
        if int(str(i)[0]) <= 5:
            for j in str(i):
                su += int(j)
            if su < 6:
                print(i)
            su = 0


fun(n)
print("Часть 2.2:")
print("----------------------")
print("Найдите минимальное число,длина факториала которого больше или равена половине N")


def fun(n):
    global mini
    for i in range(2, n + 1, 2):
        if int(str(i)[0]) <= 5:
            if len(str(math.factorial(i))) >= N // 2 and mini > i:
                mini = i


fun(n)
print(mini, ", длина факториала =", len(str(math.factorial(mini))))
