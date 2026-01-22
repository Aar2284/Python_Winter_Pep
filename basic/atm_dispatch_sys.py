amount = int(input("Enter the amount to withdraw: "))

if (amount >= 200 and amount%100 == 0 and amount != 300):
    print("Amount is Discharging")

else:
    print("Denomination not available")