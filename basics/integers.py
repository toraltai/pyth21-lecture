# privet
'============ПЕРЕМЕННАЯ============'
# переменные это ссылки на ячейки памяти, где хранятся какие то данные.
 
from this import d
from unicodedata import decimal


a = 4

" ============Ввод и вывод данных============ "
# print функция вывода данных в терминал
# input функция ввода данных с терминала
a = input()
print ("tvoe chislo", a)

"============целые числа============"
#integers(int) - целые числа (5,10,-35,9,1)
#float - вещественные (с плавающей точкой) (0.3, 0.345, 24.2)
#decimal - точное вещественное число
#чтобы использовать десимал нужно его импортировать
#complex - комплексные числа
15 // 2 #целочисленное деление (int 7)
25 ** 0,5 #квадратный корень числа
5 % 2 # остаток от деления (int 1)

#sqrt - функция для нахождения корня числа
#для работы нужно его импортировать из библ math
from math import sqrt
sqrt (36) #6
sqrt (25) #5

# модуль числа - из отрицательного числа сделает положительное ф
abs (-5) # 5

# pow:
# 1. возводит число в опреденную степень
# 2. возвращает остаток от деления результата 1 дейсвтие на третье число 

pow(2, 3) #8 = 2 **3
pow(2, 3, 4) #8 % 4 = 0
#  (2 ** 3) % 4 = 0

#divmod - функция которая принимает два числа и возвращает 2 числа, 
#где первое - это целая часть от деления, а второе остаток от деления
divmod(15, 2) # 7, 1
divmod(9, 3) # 3, 0

#round - функция которая округляет число
round(5.6) # 6
round(3.5) # 4
round(5.49) # 5 (берет первое число после .)
#можно указать сколько цифр после запятой остаток
round (10.0475, 3) # 10.048
round (10.0474, 3) # 10.047








