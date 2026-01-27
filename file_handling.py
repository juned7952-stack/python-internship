import csv

# -------------------------------
# Task 8: File Handling (TXT & CSV)
# -------------------------------

# 1. Create and write to a text file
def create_text_file():
    try:
        with open("user_data.txt", "w") as f:   # 'w' mode creates/overwrites file
            f.write("Name: Juned\n")
            f.write("Course: BTech Computer Science\n")
            f.write("Interest: Game Development & Web Development\n")
        print("Data written successfully to user_data.txt")
    except Exception as e:
        print("Error while writing:", e)

# 2. Read file contents
def read_text_file():
    try:
        with open("user_data.txt", "r") as f:   # 'r' mode for reading
            content = f.read()
            print("File Contents:\n", content)
    except FileNotFoundError:
        print("File not found!")

# 3. Append data to file
def append_text_file():
    try:
        with open("user_data.txt", "a") as f:   # 'a' mode for appending
            f.write("Hobby: Coding & Gaming\n")
        print("Data appended successfully.")
    except Exception as e:
        print("Error while appending:", e)

# 4. Handle file exceptions
def handle_exceptions():
    try:
        with open("non_existing.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("Handled Error: File does not exist.")

# 5. Create and write to a CSV file
def create_csv_file():
    try:
        with open("students.csv", "w", newline="") as f:
            writer = csv.writer(f)
            # Header
            writer.writerow(["Name", "Course", "Year"])
            # Multiple rows
            writer.writerow(["Juned", "BTech CSE", "1st Year"])
            writer.writerow(["Aman", "BTech IT", "2nd Year"])
            writer.writerow(["Sara", "BTech CSE", "3rd Year"])
        print("CSV file created successfully.")
    except Exception as e:
        print("Error while writing CSV:", e)

# 6. Read CSV data
def read_csv_file():
    try:
        with open("students.csv", "r") as f:
            reader = csv.reader(f)
            print("CSV Contents:")
            for row in reader:
                print(row)
    except Exception as e:
        print("Error while reading CSV:", e)


# -------------------------------
# Main Execution
# -------------------------------
if __name__ == "__main__":
    create_text_file()
    read_text_file()
    append_text_file()
    read_text_file()   # check after append
    handle_exceptions()
    create_csv_file()
    read_csv_file()