# challenge 18: Check if a value exists in a list

# Ask the user for a fruit name and check if it exists in a predefined list.

# fruits = ["Apple", "Mango", "Banana"]
# # User enters "Mango"
# # Output: Yes, it's in the list!


fruit_name = input("Please enter a fruit name: ")

fruits = ["Apple", "Mango", "Banana"]

if fruit_name in fruits:
    print("Yes, its in the list")
else:
    print("Not in the  list")