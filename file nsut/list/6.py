
list=[1,2,3,5,6,7]
n=int(input("enter the number to get its index "))

index=-1
for i in range(len(list)):
    if list[i]==n:
        index=i
print("the index of the element is ",index)
