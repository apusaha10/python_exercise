# Challenge 24 Task:
# Create a dictionary marks with subjects and marks:

# Math: 90  
# English: 85  
# Science: 88
# Then:

# Print the marks in English.

# Update the Science mark to 92.

# Add a new subject History with mark 80.

# Print the updated dictionary.

marks = {
    "math" : 90,
    "english" : 85,
    "science" : 88
}

print(marks["english"])

marks.update({"science": 92})
marks.update({"history": 80})


print(marks)