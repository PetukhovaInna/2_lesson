import random
x= int(input())
i=random.randint(1, 4)
if x==i:
    print("Победа")
else:
    if (x>i):
        print("Повторите ещё раз!","Загаданное число меньше")
    else:
        print("Повторите ещё раз!","Загаданное число больше")
        
