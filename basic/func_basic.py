def func():
    print("Hello World")
    print("This is a basic function.")
    print("Functions help in code reusability.")

func()

# To print same output 100 times

def func():
    for i in range(11):
        print("Hello World")
        print("This is a basic function.")
        print("Functions help in code reusability.")

func()

# Func with parameters

def func(first_name, last_name, country):
    print(f"Hello, My name is {first_name} {last_name}")
    print(f"I live in {country}")
    print("Functions Completed")

func("Aaryan", "Kalia", "India")

# Func to add 2 numbers and square the result

def func(a, b):
    return ((a+b)**2)

res = func(5,7)
print (res)

# Using list to calc sum of all the even number in that list

def func(num_list):
    even_sum = 0
    for num in num_list:
        if num % 2 == 0:
            even_sum += num
    return even_sum

result = func([4,7,765,78,65,78,79,356,678,768,54,5,444,787,67,54])

print(result)