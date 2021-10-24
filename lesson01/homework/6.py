a = int(input("Введите результат спортсмена в первый день (в км): "))
b = int(input("Введите желаемый результат (в км): "))
days = 1

while b > a:
    a = a * 1.1
    days += 1
else:
    print(days)

