# Dictonary and set related exercises


# challenge 23: Create a dictionary called contact with the following data:
#     Name: "Alice"
# Phone: "0123456789"
# Email: "alice@example.com"

# Then:

# Print the phone number.

# Add a new key "Address" with value "Dhaka" and print the updated dictionary.

info = {
    "name" : "Alice",
    "phone": "012345678",
    "email": "alice@example.com"
}

print(info["phone"])

info.update({"address" : "Dhaka"})

print(info)