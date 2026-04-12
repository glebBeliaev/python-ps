expence_car = float(input("Введите траты на автомобиль: "))
expence_food = float(input("Введите траты на еду: "))
expence_fun = float(input("Введите траты на развлечения: "))

total_expences = expence_car + expence_food + expence_fun
average_expences = total_expences / 3
print("Total expences: " + str(total_expences))
print("Average expences: " + str(average_expences))
