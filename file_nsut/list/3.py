list=[23,67,2,89]
largest=list[0]
for i in range(len(list)):
    if(list[i]>largest):
        largest=list[i]
print("the largest element in the list is ",largest)        