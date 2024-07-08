y = "kimanthi"


def mainfunction():
    global y
    print(y)

    y = "I'm a function"
    print(y)


mainfunction()
print(y)

set = {'kim', 1, 3, 'python'}
print(set)

set.add(5)
print(set)

set.remove('python')
print(set)

print(4 == 4)
print(6 > 9)
print(True or False)

print(6 > 9)
print(6 == 6)
print(True and False)


def the_outer_function():
    var = 10

    def the_inner_function():
        nonlocal var
        var = 14
        print("The value inside the inner function: ", var)

    the_inner_function()
    print("The value inside the outer function: ", var)


the_outer_function()

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is divisible by 2")

else:
    print("The number is invisible by 2")

time = float(input("Enter time :"))
if time <= 1000:
    print("You are right on Time!")

elif time <= 1020:
    print("You are late report to work \n Report to my office!!")

else:
    print("You are so inconsiderate")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = 0

my_list = [1, 2, 3, 4]
count = 1
for item in my_list:
    if item == 4:
        print("Item matched")
        count += 1
        break
print("Found at location", count)








