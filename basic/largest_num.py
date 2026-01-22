a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is (a):", a)
elif b >= a and b >= c:
    print("Largest number is (b):", b)
else:
    print("Largest number is (c):", c)