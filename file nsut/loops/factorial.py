def factorial(n):
    if(n==0 or n==1):
        return 1
    factorial=1
    for i in range(n):
        factorial=factorial*(i+1)
    return factorial
print(f"the factorial of 5 is {factorial(5)}")    