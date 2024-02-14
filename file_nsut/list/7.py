def remove_duplicate(list):
    result=[]
    for i in list:
        if i not in result:
            result.append(i)
    return result

element=[1,1,1,2,2,4,5,6]
result=remove_duplicate(element)        
print(result)
