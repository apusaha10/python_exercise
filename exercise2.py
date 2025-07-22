#  Coding challenge 2.
#  Word Length Category
#  Ask the user to input a word. Print:

#  “Short word” if it has fewer than 5 characters

#  “Medium word” if it has 5–8 characters

#  “Long word” if more than 8

word = str(input("Please enter your word: "))
length = len(word)

if (length < 5 ):
    print("Short Word")
elif(length  <= 8 ):
    print(" Medium word")
else:
    print ("Long word")
    
    
# chanllege 2 is complete