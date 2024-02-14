import math
def sum_series(x,n):
    sum=0
    for i in range(n):
        term=(((-1)**i)*(x**(2*i))/(math.factorial(2*i)))
        sum=sum+term
    return sum

print(sum_series(2,3))    

