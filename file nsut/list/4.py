list=[23,67,2,89]
smallest_item=list[0]
for i in range(len(list)):
    if(list[i]<smallest_item):
        smallest_item=list[i]
print("the smallest element in the list is ",smallest_item)        
