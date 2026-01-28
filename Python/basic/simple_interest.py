principle = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time (in years): "))

simple_interest = (principle * rate * time) / 100
print("Simple Interest is: %.2f" % simple_interest)