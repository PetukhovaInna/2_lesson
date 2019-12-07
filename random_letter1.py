import random
s=['самовар', 'весна', 'лето']
c=random.choice(s)
b=random.choice(c)
i=(c.count(b))
k=c[:i] + '?' + c[i+1:]
print(k)
buk=input('Введите букву: ')
if (buk==b):
    print('Победа!')
else:
    print('Увы!Попробуйте в другой раз.')

print('Слово:',c)
