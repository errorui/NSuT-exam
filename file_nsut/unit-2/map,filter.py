'''
Map Function:
The map function applies a given function to every item of an iterable (such as a list) and returns an iterator that yields the results. It's a fundamental tool for functional programming in Python, allowing for concise transformation of data. Here's a detailed look:

Syntax:


map(function, iterable)
Usage:

Transforms each item of an iterable using the provided function.
Returns an iterator, which can be converted to a list or iterated over directly.
'''
dummy=[1,2,3,4]
cube=list(map(lambda x:x**3,dummy))
print(cube)

'''
filter: same as map 
but instead 
return an iterator , for which function evalutates it to be true

'''
all=[for i in range(11)]
# now to make list containing only odd

odd=list(filter(lambda x:x%2!=0,all))
print(odd)