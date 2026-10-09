
import math

a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

if a == 0:
    print("Ошибка: коэффициент a не должен быть равен нулю.")
else:
    D = b ** 2 - 4 * a * c

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print("Два корня:", x1, "и", x2)
    elif D == 0:
        x = -b / (2 * a)
        print("Один корень:", x)
    else:
        print("Действительных корней нет.")