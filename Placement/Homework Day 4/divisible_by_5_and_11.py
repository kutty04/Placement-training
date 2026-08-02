num = int(input("Enter a number: "))
if num % 5==0:
    if num % 11==0:
        print("The number is divisible by both 5 and 11")
    else:
        print("The number is divisible by 5 but not by 11")
else:
    print("The number is not divisible by 5 and 11")