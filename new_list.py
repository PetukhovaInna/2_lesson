from math import sqrt
i=[2,4,9,16,25]
1)
res=[]
for x in range(len(i)):
    res.append(sqrt(i[x]))
print(res)

2)
print(list(map(lambda x: sqrt(x),i)))

3)
print([sqrt(x)for x in i])
