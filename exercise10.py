# Code challenge 10 : Ask for a single character input.
# Print if it is:

# A vowel (a, e, i, o, u)

# A consonant (any other letter)

# Not a letter at all

char = input ("Please Enter a  Character : ")
if (len(char) == 1 and char.upper() in ["A", "E", "I", "O", "U"]):
    print("The character is Vowel")
elif (len(char) == 1) and char.isalpha():
    print("This is a Consonant")
else:
    print("This is not a valid Aplphabet character")