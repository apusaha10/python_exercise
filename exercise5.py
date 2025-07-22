# Coding challenge 5. Last Digit Comparison
# Ask the user for two numbers. Compare the last digit of each number and print whether they match.


num1 = input("Enter your First Number: ")
num2 = input("Enter your Secong Number: ")

if (num1[-1] == num2[-1]):
    print("Both end With", num1[-1])
else:
    print("Different Last Digit")
    
    
# challenge 5 is complete

