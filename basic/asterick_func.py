# 2Sum using *asqrts

def sum(*args):
    total = 0
    for num in args:
        total += num
    return total
result = sum(1,2,3,4,5,6,7,8,9,10)
print(result)

# using **asqrts to add string values

def build_string(**val):
    result = ""
    for key, value in val.items():
        result += f"{key}: {value}\n"
    return result
info = build_string(name="Aaryan Kalia", 
                    country="India", 
                    field="Computer Science",
                    age=20)
print(info)

# using both *asqrts and **asqrts

def mixed_func(*args, **astrgs):
    
    print(args)
    print(astrgs)

output = mixed_func("apple", "banana", "cherry",2,4,5,6,6,3,5,3,
                    name="Aaryan Kalia",
                    country="India",
                    field="Computer Science",
                    age=20)

print(output)