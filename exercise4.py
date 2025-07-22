# 🔸 4. Multiple of 3 and 5
# Ask the user for a number and print:

# “FizzBuzz” if divisible by both 3 and 5

# “Fizz” if only divisible by 3

# “Buzz” if only divisible by 5

# “Not divisible” otherwise

num = int(input("Enter a Number: "))

if ( num%3 == 0 and num%5 == 0):
    print("FizzBuzz")
elif (num%3 == 0):
    print("Fizz")
elif (num%5 == 0):
    print("Buzz")
else:
    print("Not divisible")
    
# challenge 4 is complete