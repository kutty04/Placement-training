num = int(input("Enter a number: "))
if num % 5 == 0:
        if num % 11 == 0:
            print(f"{num} is divisible by both 5 and 11.")
        else:
            print(f"{num} is divisible by 5 but not by 11.")
else:   
    print(f"{num} is not divisible by 5.")