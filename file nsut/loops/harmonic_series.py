def harmonic_series(n):
    sum=0
    for i in range(n):
        print(f"1/{i+1}",end=" ")
        sum=sum+(1/(i+1))
    print(f"the sum is {sum}")    
harmonic_series(10)    