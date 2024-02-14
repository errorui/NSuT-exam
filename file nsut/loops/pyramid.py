index=1
def triangle(a):
    global index
    for i  in range(a):
        for j in range(a-(i+1)):
            print(" ",end =" ")
        for k in range(i+1):
            print("*",end=" ")
            
        
        for k in range(i):
            print("*",end=" ")
            
        print("")             
triangle(14)    