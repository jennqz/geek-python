proceeds = int(input("Введите сумму выручки фирмы: "))
costs = int(input("Введите сумму издержек фирмы: "))

if proceeds > costs:
    print("Фирма прибыльна.")

    profitability = (proceeds - costs) / proceeds
    print(f"Рентабельность выручки составляет {profitability}.")

    employees = int(input("Введите численность сотрудников фирмы: "))
    proceeds_per_employee = proceeds / employees

    print(f"Прибыль на одного сотрудника составляет {proceeds_per_employee}.")

else:
    print("Фирма убыточна.")