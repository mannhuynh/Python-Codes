"""
Python Gradebook
You are a student and you are trying to organize your subjects and grades using Python. 
"""

last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

# Create a list called subjects and fill it with the classes
subjects = ["physics", "calculus", "poetry", "history"]

#Create a list called grades and fill it with your scores
grades = [98, 97, 85, 88]

#After your definitions of subjects and grades but before you create gradebook, 
# use append to add "computer science" to subjects and 100 to grades.
subjects.append("computer science")
grades.append(100)

#Use the zip() function to combine subjects and grades.
# Save this zip object as a list into a variable called gradebook.
gradebook = list(zip(subjects, grades))

#After the creation of gradebook (but before you print it out), use append to add ("visual arts", 93) to gradebook.
gradebook.append(("visual arts", 93))

print(gradebook)

# You also have your grades from last semester, stored in last_semester_gradebook. 
# Create a new variable full_gradebook with the items from both gradebook and last_semester_gradebook.
full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)




