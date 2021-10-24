integer = int(input("Введите время в секундах: "))
hh = integer // 3600
a = integer % 3600
mm = a // 60
ss = a % 60
print(f"{hh:02d}:{mm:02d}:{ss:02d}")
