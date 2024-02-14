def remove(inputlist,indexlist):
    indexlist.sort(reverse=True)
    for i in indexlist:
        del inputlist[i]
    return inputlist
def remove_Even(inputlist):
    list=[]
    for i in range(len(inputlist)):
        if (i%2)==0:
           list.append(inputlist[i])
    return list       
list=[0,1,2,3,4,5,6,7]
removel=[3,5,1,2]
print(list)
print(remove_Even(list))  
print(list) 
print(remove(list,removel))    
 
