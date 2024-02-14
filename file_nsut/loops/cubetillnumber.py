def cube(n):
    return n**3
def cubetilln(n):
    for i in range(n):
        print(cube(i+1),end=" ")
    print(" ")    
cubetilln(12)    
