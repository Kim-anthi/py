print("Enter operation")
print("1. Add")
print("2. Divide")
print("3. Subtract")
print("4. Multiply")
print("5. Remainder")

operation = input()

if operation == "1":
    num1 = float(input("Enter first number"))
    num2 = float(input("Enter second number"))
    print(f"The answer is {num1 + num2}")

if operation == "2":
    num1 = float(input("Enter first number"))
    num2 = float(input("Enter second number"))
    print(f"The answer is {num1 / num2}")

if operation == "3":
    num1 = float(input("Enter first number"))
    num2 = float(input("Enter second number"))
    print(f"The answer is {num1 - num2}")

if operation == "4":
    num1 = float(input("Enter first number"))
    num2 = float(input("Enter second number"))
    print(f"The answer is {num1 * num2}")

if operation == "5":
    num1 = float(input("Enter first number"))
    num2 = float(input("Enter second number"))
    print(f"The answer is {num1 % num2}")
