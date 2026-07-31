age = int(input("Enter your age: "))
cgpa = float(input("Enter your CGPA: "))
python_score = float(input("Enter your Python Test Score: "))

if age >= 18:
    if cgpa >= 7:
        if python_score >= 70:
            print("eligible for the position.")
        else:
            print("Your Python Test Score is below 70.")
    else:
        print("Your CGPA is below 7.")
else:
    print("You must be at least 18 years old.")