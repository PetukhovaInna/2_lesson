kod=0
vrem=0
vrem=input('введите время: ')
kod=input('Введите код: ')
if kod=="343":
    gorod='Екатеринбург'
    rub=15
if kod=="381":
    gorod="Омск"
    rub=18
if kod=="473":
    gorod="Воронеж"
    rub=13
if kod=="485":
    gorod="Ярославль"
    rub=11
print (rub*int(vrem))
