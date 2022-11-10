x= list(range(10))
print(x)
x[:0]= x[-3:]
print(x)
#del x [-3:]
x[-3:]=[]
print(x)