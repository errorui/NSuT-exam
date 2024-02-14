n=int(input("enter the number of terms"))
a=0
b=1
if(n<0):
    print("not possible")
else:
    if(n==1):
        print(a)
    elif(n==2):
        print(a,end=" ")
        print(b)   
    else:
          print(a,end=" ")
          print(b,end=" ")
          while(n-2>0):
              sum=a+b
              a=b
              b=sum
              print(b,end=" ")
              n=n-1
          print(" ")    
                         