'''
As our program grows bigger, it may contain many lines of code. Instead of putting everything in a single file, we can use modules to separate codes in separate files as per their functionality. This makes our code organized and easier to maintain.

Module is a file that contains code to perform a specific task. A module may contain variables, functions, classes etc

In Python, we can also import a module by renaming it. For example,

# import module by renaming it
import math as m

print(m.pi)

# Output: 3.141592653589793

The dir() built-in function
In Python, we can use the dir() function to list all the function names in a module.


'''
import math
import Lambda as l
print(dir(math))
print(dir(l))

l.greet()
l.name_age("john wick",45)
'''
A package is a container that contains various functions to perform specific tasks. For example, the math package includes the sqrt() function to perform the square root of a number.

While working on big projects, we have to deal with a large amount of code, and writing everything together in the same file will make our code look messy. Instead, we can separate our code into multiple files by keeping the related code together in packages.

Now, we can use the package whenever we need it in our projects. This way we can also reuse our code.
'''

