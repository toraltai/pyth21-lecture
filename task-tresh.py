a = int(input('Введите первое число: '))
b = int(input('Введите первое число: '))
y = (input("Выберите операцию: '+', '-', '*', '/', '**', '//'"))
if y == '+':
    print(a + b)
elif y == '-':
    print(a - b)
elif y == '*':
    print(a * b)
elif y == '/':
    print(a / b)
elif y == '**':
    print(a ** b)
elif y == '//':
    print(a // b)