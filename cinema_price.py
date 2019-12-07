result = 0
kino=input('Введите фильм: ')
den=input('Выбрать день: ')
vrem=input('Выбрать время: ')
bilet=input('Выбрать кол-во билетов: ')
if kino=="Пятница":
    if vrem== "12":
        result=250
    elif vrem== "16":
        result=350
    elif vrem== "20":
        result=450
if kino=="Чемпионы":
    if vrem=="10":
        result=250
    elif vrem=="13":
        result=350
    elif vrem=="16":
        result=350
if kino=="Пернатая банда":
    if vrem=="10":
        result=350
    elif vrem=="14":
        result=450
    elif vrem=="18":
        result=450
if den=="Завтра":
    result=result*0.95
elif int(bilet)>=20:
    result=result*0.8
print (result*int(bilet))


