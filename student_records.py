import json

# 1. Create dictionary to store student details
students = {
    "101": {"name": "Aarav", "age": 20, "course": "Computer Science"},
    "102": {"name": "Meera", "age": 21, "course": "Information Technology"},
    "103": {"name": "Rohan", "age": 19, "course": "Electronics"}
}

# 2. Access keys and values
print("All Student IDs:", students.keys())
print("All Student Details:", students.values())

# 3. Update an entry
students["102"]["course"] = "Data Science"

# 4. Delete an entry
del students["103"]

# 5. Loop through dictionary
print("\nFormatted Student Records:")
for student_id, details in students.items():
    print(f"ID: {student_id}, Name: {details['name']}, Age: {details['age']}, Course: {details['course']}")

# 6. Convert dictionary to JSON
students_json = json.dumps(students, indent=4)

# 7. Save JSON to file
with open("students.json", "w") as f:
    f.write(students_json)

# 8. Read JSON back into Python
with open("students.json", "r") as f:
    loaded_students = json.load(f)

# 9. Print clean formatted output
print("\nLoaded Student Records from JSON:")
for student_id, details in loaded_students.items():
    print(f"ID: {student_id}, Name: {details['name']}, Age: {details['age']}, Course: {details['course']}")