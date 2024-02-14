def average_sum():
    number=[]
    sum=0
    for i in range(10):
        a=int(input(f"enter the {i+1} number "))
        sum=sum+a
        number.append(a)
    print(f"the sum of numbers is {sum}")    
    print(f"the average of numbers is {sum/len(number)}")    

average_sum()    