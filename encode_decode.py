import math
import random
def encode(s):
    if(len(s)>3):
        
        s=s[1:]+s[0]
       
        for i in range(3):
            random_num=random.randint(0, 25)
            ascii_value_a = ord('a')
            result = chr(ascii_value_a + random_num)
            s = result + s
        for i in range(3):
            random_num=random.randint(0, 25)
            ascii_value_a = ord('a')
            result = chr(ascii_value_a + random_num)
            s = s+result
    else:
        s=s[-1::-1]
    return s          
def decode(s):
    if(len(s)<=3):
        return s[-1::-1]
    else:
        s=s[3:-3]
        
        s=s[-1]+s[:-1]
        return s

while True:    
 print('''
  Do you want to encode or decode?
       1.encode
       2.decode
 
 ''')
 
 try:
     user_input=int(input(" enter the choice: "))
     if user_input == 1:
         s = str(input("Enter the string: "))
         print(f"The encoding of {s} is {encode(s)}")
     elif user_input == 2:
         s = str(input("Enter the string: "))
         print(f"The decoding of {s} is {decode(s)}")
     else:
         print("Invalid choice. Enter 1 or 2.")
 
 except ValueError:
        print("Enter integers only.")

 finally:
     b=input("want to continue y/n :")
     if b=='n':
        break
     if b=='y':
       print("\n \n")
     else:
         print("invalid choice")  
 

# 
