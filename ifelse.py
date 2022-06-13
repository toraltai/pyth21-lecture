"==============Логические операторы=============="
# логические операторы - выражения, которые возвращают True, если правда, False - если ложь
5 == 5 #True
4 == 5 #False

5!= 5 #False
5 != 2 #True

5 > 10 #False
10 > 5 #True

5 <= 10 #True
10 <=5 #False
5 <= 5 #True

5 >= 10 #False
10 >= 5 #True
5 >= 5 #True

'5' == 5 #False

"==============Boyal Type=============="
#Булевый тип данных - имеет всего 2 значения True & False
bool(1) #True
bool(0) #False
bool(-277) #True

bool('Hello') #True
bool('') #False
bool(' ') #True

bool(True) #True
bool(False) #False


"==============None Type=============="
# none - тип данных с одним значением None, который используется для обозначения пустых значений или отсутствие значений.
bool(None) #False
bool('None') #True

a = None
print(bool(a)) #False
print(a is None) #True
#is это проверка на полное соответсвие


"==============Условные Операторы=============="
a = int(input("Type Num: "))
if a>0:
    print (f'Число{a} - положительное')
elif a<0:
    print (f'Число{a} - отрицательое')
else:
    print (f'Число{a} - это 0')

# условные операторы нужны для того, чтобы при разных данных код работал по разному


"==============Тернарные операторы=============="
#условия в одну строку
тело1 if условие else тело2

res = 'Hello' if a == 5 else 'Bye' 
print(res) 
# Hello, если a == 5
# Bye, если a != 5