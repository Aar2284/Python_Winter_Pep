# print prime numbers between 1 to n

n = int(input("Enter a number: "))

for num in range(1, n + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if (num % i) == 0:
                break
            
        else:
            print(num)

# odd numbers between 1 to n

print("Odd numbers between 1 to", n, "are:")
for num in range(1, n + 1):
    if num % 2 != 0:
        print(num)

# even numbers between 1 to n

print("Even numbers between 1 to", n, "are:")
for num in range(1, n + 1):
    if num % 2 == 0:
        print(num)

