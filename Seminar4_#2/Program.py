 #Задача 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

#************************
def primeFactorsList(num):
    i = 2
    lst = []
    while i <= num:
        if num % i == 0:
            lst.append(i)
            num //= i
            i = 2
        else:
            i += 1
    return lst

#************************
import os 
os.system('cls')

print("Программа составляет список простых множителей числа N.")
N = int(input("Введите число N: "))

lst = primeFactorsList(N)

print(f"Список {lst} простых множителей числа {N}")