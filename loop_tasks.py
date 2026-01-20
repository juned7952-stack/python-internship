# loop_tasks.py
# Task 4: Loops & Iterations
# Author: Juned

# 1. For loop to print numbers 1-100
print("Numbers from 1 to 100:")
for i in range(1, 101):
    print(i, end=" ")
print("\n" + "-"*50)

# 2. While loop for countdown timer
print("Countdown from 10:")
count = 10
while count >= 0:
    print(count)
    count -= 1
print("Blast Off!\n" + "-"*50)

# 3. Break and Continue demonstration
print("Break and Continue Example:")
for i in range(1, 11):
    if i == 5:
        print("Skipping 5 using continue")
        continue
    if i == 8:
        print("Breaking loop at 8")
        break
    print(i)
print("-"*50)

# 4. Iterate over string characters
sample_string = "Python"
print("Iterating over string characters:")
for char in sample_string:
    print(char)
print("-"*50)

# 5. Multiplication table (for 7)
print("Multiplication Table of 7:")
for i in range(1, 11):
    print(f"7 x {i} = {7*i}")
print("-"*50)

# 6. Range with steps
print("Range with steps (even numbers 2-20):")
for i in range(2, 21, 2):
    print(i, end=" ")
print("\n" )

# 7. Combine loop with conditions
print("Odd and Even check from 1-10:")
for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} is Even")
    else:
        print(f"{i} is Odd")
print("-"*50)

# 8. Real-world example: Sum of marks
marks = [85, 90, 78, 92, 88]
total = 0
for mark in marks:
    total += mark
average = total / len(marks)
print("Marks:", marks)
print("Total Marks:", total)
print("Average Marks:", average)
print("-"*50)

