n = int(input("Enter the number of rows for the star pattern: "))

# Star pattern
for i in range(1, n + 1):
    print("*" * i)

# Number pattern
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Reverse number pattern
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Reverse star pattern
for i in range(n, 0, -1):
    print("*" * i)

# Pyramid star pattern
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

# Inverted pyramid star pattern
for i in range(n, 0, -1):
    print(" " * (n - i) + "* " * i)

# Diamond star pattern
for i in range(1, n + 1):   
    print(" " * (n - i) + "* " * i)

# Lower half of diamond
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)

# Hollow square star pattern
for i in range(1, n + 1):   
    for j in range(1, n + 1):
        if i == 1 or i == n or j == 1 or j == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Hollow right-angled triangle star pattern
for i in range(1, n + 1):   
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Hollow pyramid star pattern
for i in range(1, n + 1):   
    for j in range(1, n - i + 1):
        print(" ", end=" ")
    for k in range(1, 2 * i):
        if k == 1 or k == 2 * i - 1 or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Hollow diamond star pattern
for i in range(1, n + 1):   
    for j in range(1, n - i + 1):
        print(" ", end=" ")
    for k in range(1, 2 * i):
        if k == 1 or k == 2 * i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Lower half of hollow diamond
for i in range(n - 1, 0, -1):   
    for j in range(1, n - i + 1):
        print(" ", end=" ")
    for k in range(1, 2 * i):
        if k == 1 or k == 2 * i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Full pyramid number pattern
for i in range(1, n + 1):   
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Inverted full pyramid number pattern
for i in range(n, 0, -1):   
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Diamond number pattern
for i in range(1, n + 1):   
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Lower half of diamond number pattern
for i in range(n - 1, 0, -1):   
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Pascal's triangle pattern
for i in range(n):   
    print(" " * (n - i), end="")
    coeff = 1
    for j in range(i + 1):
        print(coeff, end=" ")
        coeff = coeff * (i - j) // (j + 1)
    print()

# Inverted Pascal's triangle pattern
for i in range(n - 1, -1, -1):   
    print(" " * (n - i), end="")
    coeff = 1
    for j in range(i + 1):
        print(coeff, end=" ")
        coeff = coeff * (i - j) // (j + 1)
    print()

# Diamond Pascal's triangle pattern
for i in range(n):   
    print(" " * (n - i), end="")
    coeff = 1
    for j in range(i + 1):
        print(coeff, end=" ")
        coeff = coeff * (i - j) // (j + 1)
    print()

# Lower half of diamond Pascal's triangle pattern
for i in range(n - 1, -1, -1):   
    print(" " * (n - i), end="")
    coeff = 1
    for j in range(i + 1):
        print(coeff, end=" ")
        coeff = coeff * (i - j) // (j + 1)
    print()