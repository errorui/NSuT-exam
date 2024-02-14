def isodd(n):
    if(n%2==0):
        return False
    return True
def sumofodd(n):
    sum=0
    for i in range(n):
        if(isodd(i+1)):
            
            sum=sum+(i+1)
    return sum

print(sumofodd(15))