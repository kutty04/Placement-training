age = int(input("Enter your age: "))
cgpa = float(input("Enter your CGPA: "))

if age >= 18:
    if cgpa >= 7:
        print("Eligible for Placement")
    else:
        print("CGPA requirement not met")
else:
    print("Age requirement not met")