num = int(input("Enter first number"))
num2 = int(input("Enter second number"))
num3 = int(input("Enter third number"))
num4 = int(input("Enter fourth number"))

if num > num2 and num > num3 and num > num4:
    print(f"the largest")
#elif num > num2 and num > num3 and num > num4:
#   print(f"the smallest number is {num}")

elif num2 > num and num2 > num3 and num2 > num4:
    print(f"the largest number is {num2}")
#elif num2 > num and num2  > num3 and num2 > num4:
#   print(f"the smallest number is {num2}")

elif num3 > num and num3 > num2 and num3 > num4:
    print(f"the largest number is{num3}")
#elif num3 > num and num3 > num2 and num3 > num4:
#   print(f"the smallest number is {num3}")

if num4 > num and num4 > num2 and num4 > num3:
    print(f"the largest number is {num4}")
# elif num4 > num and num4 > num2 and num4 > num3:
# print(f"the smallest number is {num4}")
else:
    print(f"the largest number is {num4}")
