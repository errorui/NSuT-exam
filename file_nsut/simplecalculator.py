
a=int(input("enter the first number :"))
b=int(input("enter the second number :"))
print('''
  chose the operation to be performed
      1:addition (+)
      2:subtraction (-)
      3:multiplicate (*)
      4:division (/)
''')
operation=input(" enter ")
validoperation=["+","-","*","/"]
if operation not in validoperation:
    print("sorry enter the right operation only")
else:
    if(operation=="+"):
        print(f"the addition of {a} and {b} is {a+b}")
    if(operation=="-"):
        print(f"the subtraction of {a} and {b} is {a-b}")
    if(operation=="*"):
        print(f"the multiplication of {a} and {b} is {a*b}")
    if(operation=="/"):
        print(f"the division of {a} and {b} is {a/b}")