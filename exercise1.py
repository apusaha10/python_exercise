# 🔸 1. Grade Calculator
# Ask the user for a number between 0 and 100 and print the grade:

# 90-100: A

# 80-89: B

# 70-79: C

# 60-69: D

# <60: F
# Also check if the number is outside the 0–100 range and print “Invalid input”.


num = int(input("Please Enter your Number: "))      # a variable is created to take input form

if ( num < 0  or num > 100):
    print("Your Number is not valid , Please Enter a Number Between 0 and 100")
else:
    if ( num >= 90 ):
        grade = "A"
    elif( num >= 80 ):
        grade = "B"
    elif ( num >= 70 ):
        grade = "C"
    elif (num >= 60 ):
        grade = "D"
    else:
        grade = "F"

    print( "Your grade is ",grade )
    
    
# 1st challenege is done
