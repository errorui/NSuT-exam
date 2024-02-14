def add(tur,item):
    y=list(tur)
    y.append(item)
    x=tuple(y)
    return x
t=(1,2,4,"r")
t=add(t,"add")
print(t)

def tupletostring(tur):
    a=""
    for i in tur:
        a=a+i
         
    print(a)
t2=('r','a','j',' ','r','a','m')         
tupletostring(t2)
print(t2[::-1])