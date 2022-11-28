 #Задача 1. Вычислить число c заданной точностью d.

#************************
def accuracy(d) -> float:
    import math
    from math import pi
    return round(pi, d)

#************************
import os 
os.system('cls')

print("Программа вычисляет число π c заданной точностью d.")
d = int(input("Введите желаемую точность числа π: "))

acc = accuracy(d)

print(f"При заданной точности {d} число π будет: {acc}")