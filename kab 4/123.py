import random
#punkty=[]
#for a in range(15):
    #p=random.uniform(0,50)
    #p=round(p,2)
    #punkty.append(p)
punkty=[round(random.uniform(0,50),2) for a in range(15)]
print(punkty)
print(f'Wartośc minimalna wynosi: {min(punkty)}')
print(f'Wartośc maksymalna wynosi: {max(punkty)}')
a = float(input("Podaj wybraną liczbę z listy: "))
if a in punkty:
    print(punkty.index(a))
else:
    print("Liczba nie występuje na liście")

for s in punkty:
    if s>srednia:
        powyzej.append(s)
print(powyzej,len(powyzej))
ponizej=[s for s in punkty if s<srednia]
print(ponizej,len(ponizej))

