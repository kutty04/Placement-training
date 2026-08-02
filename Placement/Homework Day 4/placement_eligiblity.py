age = int(input("Enter your age: "))
cgpa = float(input("Enter your CGPA:"))
python_score = int(input("Enter your Python score:"))
if age >=18:
    if cgpa >= 7.5:
        if python_score >=50:
            print("Congatulation! You are eligible for placement.")
        else:
            print("Not selected, Your python score is less than 50")
    else:
        print("Not selected, Your CGPA is less than 7.5")
else:
    print("Not selected, Your age should be at least 18:")