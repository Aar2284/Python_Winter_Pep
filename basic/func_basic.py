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

# Func to check if a number is prime or not

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")

else:
    print(f"{number} is not a prime number.")

# Profile building using functions

def build_profile(first_name, last_name, **user_info): # **user_info -> used to pass variable length of arguments
    profile = {}
    profile['first_name'] = first_name
    profile['last_name'] = last_name
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('Aaryan', 'Kalia',
                             location='India',
                                field='Computer Science',
                                age=20)

print(user_profile)