# lambda function 

square = lambda x: x * x
print(square(5))

# lambda with 2 parameters for addition

add = lambda x, y: x + y
print(add(5, 10))

# function to find max of 2 numbers using lambda

max_num = lambda a, b: a if a > b else b
print(max_num(10, 20))

# lambda with map function to square a list of numbers

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)

# lambda to filter even numbers from a list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# reduce function to find the product of a list of numbers using lambda

from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)