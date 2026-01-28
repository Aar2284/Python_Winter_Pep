Time = float(input("Enter the time in 24 hour format: "))

if Time > 24:
    print("Invalid Time")

elif Time < 12:
    print("Good Morning")

elif 12 <= Time < 18:
    print("Good Afternoon")

elif 18 <= Time < 21:
    print("Good Evening")

else:
    print("Good Night") 