# Demonstration of Python data types
# Integer
int_var = 42
print(f"Integer: {int_var}, Type: {type(int_var)}")

# Float
float_var = 3.14
print(f"Float: {float_var}, Type: {type(float_var)}")

# String
str_var = "Hello, World!"
print(f"String: {str_var}, Type: {type(str_var)}")

# Boolean
bool_var = True
print(f"Boolean: {bool_var}, Type: {type(bool_var)}")

#arithmetic operations
a = 10
b = 5   
sum_result = a + b       #Addition
diff_result = a - b      #Subtraction
prod_result = a * b       #Multiplication
div_result = a / b       #Division
print(f"Sum: {sum_result} \n, Difference: {diff_result}, Product: {prod_result}, Division: {div_result}")

#CONVERTING STRINGS TO INTEGERS AND FLOATS
str_num = "100"
int_num = int(str_num)
float_num = float(str_num)
print(f"String: {str_num} \n, Converted to Integer: {int_num}, Converted to Float: {float_num}")

#Concatenation of strings
str1 = "Hello"  
str2 = "World"
concat_str = str1 + " " + str2
print(f"Concatenated String: {concat_str}")

#dynamic typing
var = 10                   # Initially an integer
print(f"Initial Value: {var}, Type: {type(var)}")
var = "Now I'm a string"    # Now a string
print(f"New Value: {var}, Type: {type(var)}")

#invalid input using basic error handling
user_input = input("Enter a number: ")
try:
    num = int(user_input)
    print(f"You entered the number: {num}")   
except ValueError:
    print("Invalid input! Please enter a valid integer.")