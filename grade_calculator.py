# Grade Calculator using Conditional Statements

marks = int(input("Enter your marks (0 - 100): "))

# Check for invalid marks
if marks < 0 or marks > 100:
    print("Invalid marks! Please enter marks between 0 and 100.")

# Grade conditions
elif marks >= 90 and marks <= 100:
    print("Grade A+ : Excellent")

elif marks >= 80 and marks < 90:
    print("Grade A : Very Good")

elif marks >= 70 and marks < 80:
    print("Grade B : Good")

elif marks >= 60 and marks < 70:
    print("Grade C : Average")

elif marks >= 40 and marks < 60:
    print("Grade D : Needs Improvement")

else:
    print("Grade F : Fail")