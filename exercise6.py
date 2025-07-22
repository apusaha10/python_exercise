# coding challenge 6: Ask for a string. If it starts with “A” or “a” and ends with “Z” or “z”, print a special message.

word = input("Enter a word or sentence: ")
word1 = word[0]
word2 = word[-1]

if (word1.upper() == "A" and word2.upper() == "Z"):
    print("You are a special Person")
else:
    print("Please try again")
    
    
# Challenge 6 is completed 