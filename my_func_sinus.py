import math
value = input("Введите x: ")
if value:
    x= float(value)
    if 0.2<=x<=0.9:
        print(math.sin(x))
    else:
        print(1)
else:
    print("Введите значение x!")
