list2=[1,2,35,4]
list1=list2.copy()

print(list1)

numbers = [1, 2, 3, 4, 5]

# Applying map and filter directly
squared = map(lambda x: x**3, numbers)
filtered = filter(lambda x: x > 8, squared)
print(list(filtered)) # Output: [27, 64, 125]

print(list(squared))

