# 🔸 1. Grade Calculator
# Ask the user for a number between 0 and 100 and print the grade:

# 90-100: A

# 80-89: B

# 70-79: C

# 60-69: D

# <60: F
# Also check if the number is outside the 0–100 range and print “Invalid input”.


num = int(input("Please Enter your Number: "))      # a variable is created to take input form

if ( num >= 90 and num <= 100 ):
    print(" Grade : A")