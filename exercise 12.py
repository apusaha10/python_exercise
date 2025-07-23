# challenge 12: Task: Ask the user for 5 numbers, store them in a list, and print how many are even and how many are odd.

numbers = []

num1 = input("Please enter first number")
num2 = input("Please enter second number")
num3 = input("Please enter third number")
num4 = input("Please enter Fourth number")
num5 = input("Please enter Fifth number")

numbers.append(num1)
numbers.append(num2)
numbers.append(num3)
numbers.append(num4)
numbers.append(num5)

if (numbers%2 == 0):
    print("Numbers are even")
else:
    print("odd numbers")
