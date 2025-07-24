# challenge 21: Get the second item from a list entered by the user
# Ask the user to enter 3 items (e.g., favorite colors), store them in a list, and print the second one.


item = []

item1 = input("Please enter your 1st favorite color: ")
item2 = input("Please enter your 2nd favorite color: ")
item3 = input("Please enter your 3rd favorite color: ")

item.append(item1)
item.append(item2)
item.append(item3)

print(item[1])
