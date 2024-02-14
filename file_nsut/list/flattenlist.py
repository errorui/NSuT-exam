def flattenlist(input_list,answer):
    for i in input_list:
        if isinstance(i,list):
            flattenlist(i,answer)
        else:
            answer.append(i)
shallow_list = [1, [2, 3], [4, 5], 6]         
answer=[]
flattenlist(shallow_list,answer)
print(answer)       

list2=[7,8,9]
answer.extend(list2)
print(answer)
def is_circular(list1,list2):
    if(len(list1)!=len(list2)):
        return False
    concated=list1+list1
    for i in range(len(list1)):
        if list2 == concated[i:i+len(list1)]:
            return True
    return False
list1 = [1, 2, 3, 4]
list2 = [3, 4, 1, 2]

if is_circular(list1, list2):
    print("The lists are circularly identical.")
else:
    print("The lists are not circularly identical.")    