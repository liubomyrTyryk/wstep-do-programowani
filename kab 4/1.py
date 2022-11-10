zestaw_1=[]
import random
y = int(input("podaj liczbe elemtnow listy"))
for i in range(y):
    x = random.randint(1,10)
    zestaw_1.append(x)
print(zestaw_1)


j=int(input("podaj liczbe elemtnow listy"))
zestaw_2=[random.randint(5,15) for i in range(j)]
print(zestaw_2)

f=int(input("poday liczbe:"))
if f in zestaw_1:
    print("Liczba z zestawu 1 występuje")
elif f in zestaw_2:
    print('Liczba z zestaw 2 wystęnpuje')
else:
    print('nie ma takiej liczby')


zestaw_1_2=zestaw_1+zestaw_2
print(zestaw_1_2)
zestaw_1_2.sort()
print(zestaw_1_2)