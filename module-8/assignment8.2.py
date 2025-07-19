#Blaise A. Johnson
#July 19, 2025
#Assignment 8.2

#The purpose of this program is it manage and update a list stored in the given json file.


import json


file_path = "student.json"

# Prints student lsit
def print_students(students):
    for student in students:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")
        
#opens and loads json file
with open(file_path, "r") as file:
    student_list = json.load(file)

# original notification
print("\n--- Original Student List ---")
print_students(student_list)

# added student
new_student = {
    "F_Name": "Blaise",
    "L_Name": "Johnson",
    "Student_ID": 40402,
    "Email": "blaise.johnson@gmail.com"
}
student_list.append(new_student)

# updated list notification 
print("\n--- Updated Student List ---")
print_students(student_list)


with open(file_path, "w") as file:
    json.dump(student_list, file, indent=4)

print("\nThe student.json file has been updated.")

