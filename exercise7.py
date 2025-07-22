# 7. Number as String Length
# Ask the user to input a number (as a string), then:

# Check if the number has 2 digits

# Print the sum of its digits (as integers)


num = input("Enter Number: ")

if (len(num) == 2):
    print (int(num[0]) + int(num[1]))
else:
    print("Please Enter a two digit Number")