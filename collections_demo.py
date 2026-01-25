# collections_demo.py
# -------------------------------
# 1. LIST DEMO
# -------------------------------

# Store student names in a list
students = ["Aman", "Riya", "Karan", "Riya", "Neha"]

print("Original List:", students)

# Add element
students.append("Zoya")
print("After Adding Zoya:", students)

# Remove element
students.remove("Karan")
print("After Removing Karan:", students)

# Sort list
students.sort()
print("Sorted List:", students)

# Iterate over list
print("Iterating over List:")
for s in students:
    print("-", s)

# -------------------------------
# 2. TUPLE DEMO
# -------------------------------

# Tuple for fixed data (immutable)
course_info = ("Python Developer Internship", "Elevate Labs", "MSME")

print("\nTuple Data:", course_info)
print("Accessing Tuple Element:", course_info[0])

# -------------------------------
# 3. SET DEMO
# -------------------------------

# Convert list to set to remove duplicates
unique_students = set(students)
print("\nUnique Students (Set):", unique_students)

# Add element to set
unique_students.add("Ishaan")
print("After Adding Ishaan:", unique_students)

# Remove element from set
unique_students.discard("Riya")
print("After Removing Riya:", unique_students)

# Set operations
groupA = {"Aman", "Neha", "Zoya"}
groupB = {"Neha", "Ishaan", "Riya"}

print("\nUnion:", groupA | groupB)
print("Intersection:", groupA & groupB)
print("Difference (A - B):", groupA - groupB)

# Iterate over set
print("Iterating over Set:")
for name in unique_students:
    print("-", name)

# -------------------------------
# 4. MUTABLE vs IMMUTABLE
# -------------------------------

print("\nMutable vs Immutable:")
print("List before change:", students)
students[0] = "Arjun"  # Lists can be changed
print("List after change:", students)

print("Tuple before change:", course_info)
# course_info[0] = "New Internship"  # ❌ This will throw error
print("Tuples cannot be modified once created!")

# -------------------------------
# 5. FORMATTED OUTPUT
# -------------------------------

print("\nFinal Summary:")
print(f"Total Students: {len(students)}")
print(f"Unique Students: {len(unique_students)}")
print(f"Course Info: {course_info}")