def largestofthree( a, b, c):
     f1=0
     if(a>b):
          f1=a
     else:
          f1=b

     if(f1>c):
          return f1
     else:
          return c
               

a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))

print(f"the greatest out {a},{b} and {c} is {largestofthree(a,b,c)}")
