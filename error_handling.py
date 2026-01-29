# error_handling.py
import logging

# Configure logging: save logs to a file
logging.basicConfig(
    filename="app.log",              # log file name
    level=logging.DEBUG,             # log everything (DEBUG and above)
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Custom exception class
class NegativeNumberError(Exception):
    """Raised when a negative number is not allowed"""
    pass

def divide_numbers(a, b):
    try:
        logging.info("Trying to divide %s by %s", a, b)
        result = a / b
    except ZeroDivisionError:
        logging.error("Division by zero error occurred!")
        print("You cannot divide by zero.")
    except TypeError:
        logging.error("Type error: inputs must be numbers.")
        print(" Please enter valid numbers only.")
    else:
        logging.info("Division successful. Result = %s", result)
        print(f" Division successful! Result = {result}")
    finally:
        logging.info("Execution of divide_numbers completed.")
        print(" Finished attempting division.")

def square_root(n):
    try:
        logging.info("Trying to calculate square root of %s", n)
        if n < 0:
            raise NegativeNumberError("Negative numbers not allowed for square root.")
        result = n ** 0.5
    except NegativeNumberError as e:
        logging.error("Custom Error: %s", e)
        print(f" Error: {e}")
    else:
        logging.info("Square root successful. Result = %s", result)
        print(f" Square root of {n} is {result}")
    finally:
        logging.info("Execution of square_root completed.")
        print(" Finished attempting square root.")

# Simulate runtime errors
if __name__ == "__main__":
    print("=== Exception Handling & Logging Demo ===\n")

    # Case 1: Division by zero
    divide_numbers(10, 0)

    # Case 2: Invalid type
    divide_numbers("10", 2)

    # Case 3: Successful division
    divide_numbers(20, 5)

    # Case 4: Negative number for square root
    square_root(-9)

    # Case 5: Successful square root
    square_root(16)

    print("\nCheck 'app.log' file for detailed logs.")