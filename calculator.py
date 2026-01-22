
def add(a,b) :
    #Return the sum of two numbers.
    return a + b

def subtract(a,b) -> float:
    #Return the difference of two numbers."
    return a - b

def multiply(a,b) -> float:
    #Return the product of two numbers."
    return a * b

def divide(a,b) -> float:
    #Return the division of two numbers. Handles division by zero.
    if b == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return a / b

def calculator():
    # Main calculator function to handle user choice and call operations.
    print("Welcome to Modular Calculator \nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    if choice == '1':
        print("Result: " + str(add(num1, num2)))
    elif choice == '2':
        print("Result: " + str(subtract(num1, num2)))
    elif choice == '3':
        print("Result: " + str(multiply(num1, num2)))
    elif choice == '4':
        result = divide(num1, num2)
        if result is not None:
            print("Result: " + str(result))
    else:
        print("Invalid choice. Please select from 1 to 4.")

calculator()