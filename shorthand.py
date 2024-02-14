a = 330000
b = 3300809
print("A") if a > b else print("=") if a == b else print("B","hr")

c = 9 if a>b else 0
print(c)

fruits = ['apple', 'banana', 'mango']
for fla in fruits:
    print(fla)
for index, fruit in enumerate(fruits,start=1):
    print(index, fruit)
my_dict = {'a': 1, 'b': 2, 'c': 3}

for index, (key, value) in enumerate(my_dict.items(),start=1):
    print(f"Index: {index}, Key: {key}, Value: {value}")    