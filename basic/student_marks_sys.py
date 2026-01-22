Student_Name = input("Enter Student Name (ID): ")

Math_Marks = float(input("Enter Marks obtained in Mathematics: "))
Science_Marks = float(input("Enter Marks obtained in Science: "))
English_Marks = float(input("Enter Marks obtained in English: "))
Computer_Marks = float(input("Enter Marks obtained in Computer: "))
SST_Marks = float(input("Enter Marks obtained in Social Studies: "))
    

Total_Marks = Math_Marks + Science_Marks + English_Marks + Computer_Marks + SST_Marks
Average = Total_Marks / 5

print("Student Name (ID):", Student_Name)
print("Total Marks:", Total_Marks)
print("Average Marks: %.2f" % Average)

print("Result Status:", "Pass" if Average >= 40 else "Fail")
print("Result Calculation Completed")