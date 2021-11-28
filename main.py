# Создание списка из чисел до 50, реверс списка
lst = []
for i in range(50):
    lst.append(i+1)
    lst.sort(reverse=True)

# Добвление сторон и остальных переменных(максимальная площадь - s_max, полупериметр - polyper)
first = lst[0]
second = lst[1]
s_max = 0
polyper = 0
stor_max = []

# Создание условий существования треугольника, вычисление его площади
for i in range(2, len(lst)):
    if second + lst[i] > first and first + second > lst[i] and first + lst[i] > second:
        polyper = (first + second + lst[i]) / 2
        s_max = (polyper*(polyper-first)*(polyper-second)*(polyper-lst[i])) ** 0.5
        stor_max = [first, second, lst[i]]

        # вывод максимальной площади и сторон треугольника
        print("Стороны треугольника", stor_max)
        print("max площадь ", s_max)
    else:
        print("Треугольник не существует")
    break
