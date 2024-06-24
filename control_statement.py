from functions import addtwonumber

age = int(input("Enter Age: "))

if age >= 18:
    print(f"You are eligible to vote")
else:
    print(f"Sorry You are under age")

num = int(input("Enter number: "))

if num % 2 == 0:
    print(f"The number is even: ")
else:
    print(f"The number is odd")
