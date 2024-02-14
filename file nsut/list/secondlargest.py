def secondlargest(list):
    copylist=list[:]
    copylist.sort()
    return copylist[len(copylist)-2]
list=[1,25,67,99,2]
print(f"the second larges value in list is {secondlargest(list)}")

list2=[1,2,1,1,3,5,5,4,6,64,100,100,100]
def occurence(list):
    map={}
    for i in list:
        if i not in map:
            map[i]=1
        else:    
         map[i]=map[i]+1
    print(map)
occurence(list2)        