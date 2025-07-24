# challenge 12: Task: Ask the user for 5 numbers, store them in a list, and print how many are even and how many are odd.

# Take 5 numbers from user
numbers = []
num1 = int(input("Please enter first number: "))
num2 = int(input("Please enter second number: "))
num3 = int(input("Please enter third number: "))
num4 = int(input("Please enter fourth number: "))
num5 = int(input("Please enter fifth number: "))

numbers.append(num1)
numbers.append(num2)
numbers.append(num3)
numbers.append(num4)
numbers.append(num5)

even_count = 0
odd_count = 0

# Loop through the list to count even and odd numbers
for number in numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Total even numbers:", even_count)
print("Total odd numbers:", odd_count)
