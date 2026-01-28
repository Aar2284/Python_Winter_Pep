print("Welcome to Shopping Cart System")

Item1 = input("Item 1 Name: ")
Cost1 = float(input("Cost of Item1: "))
Quantity1 = int(input("Number of Purchase: "))

Total1 = Quantity1*Cost1
print(Total1)

Item2 = input("Item 2 Name: ")
Cost2 = float(input("Cost of Item2: "))
Quantity2 = int(input("Number of Purchase: "))

Total2 = Quantity2*Cost2
print(Total2)

Item3 = input("Item 3 Name: ")
Cost3 = float(input("Cost of Item3: "))
Quantity3 = int(input("Number of Purchase: "))

Total3 = Quantity3*Cost3
print(Total3)

Total_Amnt = Total1 +Total2 + Total3

Final_Amnt = Total_Amnt + (0.18 * Total_Amnt)

print("Final Amount: ",Final_Amnt)