 #Задача 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

#************************
def nonRepetitive(lstIsh):
    lst = []
    for i in lstIsh:
        if lstIsh.count(i)==1:
            lst.append(i)
    return lst

#************************
import os 
os.system('cls')

print("Программа выводит список неповторяющихся элементов исходной последовательности, заданной пользователем.")
lstIsh = list(map(int, input("Введите числа исходной последовательности через пробел:\n").split()))

lst = nonRepetitive(lstIsh)

print(f"В исходном списке {lstIsh} содержатся следующие неповторяющиеся элементы {lst}")