cost = float(input("Введите стоимость одной минуты разговора: "))
minutes = float(input("Введите длительность разговора в минутах: "))
day = input("Введите день недели: ").lower()

total = cost * minutes

if day == "суббота" or day == "воскресенье":
    total = total * 0.8

print("Стоимость разговора:", round(total, 2), "руб.")