# Lambda Functions
# Lambda functions are small, anonymous functions defined using the lambda keyword.
# They can have any number of arguments but only one expression.
# They are often used as arguments to higher-order functions like map and filter.
# hey are particularly useful when you need a simple function for a short period of time. The syntax is lambda arguments: expression
greet=lambda:print("hello world")
# greet()
name_age=lambda name,age:print(f"your name is {name} and age is {age}")
# name_age("john doe",25)