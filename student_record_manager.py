import re

FILE_NAME = "students.txt"

EMAIL_PATTERN = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"


def is_valid_email(email):
    """Validate an email address using regular expression."""
    return re.match(EMAIL_PATTERN, email) is not None


def add_student():
    """Get student details, validate them, and save them to a file."""
    try:
        print("\n--- Add Student ---")

        student_id = input("Enter Student ID: ").strip()
        name = input("Enter Student Name: ").strip()
        email = input("Enter Email: ").strip()

        if not student_id or not name or not email:
            raise ValueError("All fields are required.")

        if not is_valid_email(email):
            raise ValueError("Invalid email format.")

        with open(FILE_NAME, "a", encoding="utf-8") as file:
            file.write(f"{student_id},{name},{email}\n")

        print("Student data saved successfully.")

    except ValueError as error:
        print("Invalid input:", error)
    except OSError as error:
        print("File error:", error)


def read_students():
    """Read and display all student records from the file."""
    try:
        print("\n--- Student Records ---")

        with open(FILE_NAME, "r", encoding="utf-8") as file:
            records = file.readlines()

        if not records:
            print("No student records found.")
            return

        for record in records:
            student_id, name, email = record.strip().split(",", 2)
            print(f"ID: {student_id} | Name: {name} | Email: {email}")

    except FileNotFoundError:
        print("No student data file found. Add a student first.")
    except OSError as error:
        print("File error:", error)
    except ValueError:
        print("Invalid record found in the data file.")


def main():
    """Main menu for the Student Record Manager."""
    while True:
        print("\n===== STUDENT RECORD MANAGER =====")
        print("1. Add Student")
        print("2. Read Student Data")
        print("3. Exit")

        try:
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                add_student()
            elif choice == "2":
                read_students()
            elif choice == "3":
                print("Thank you!")
                break
            else:
                raise ValueError("Please enter 1, 2, or 3.")

        except ValueError as error:
            print("Invalid input:", error)
        except KeyboardInterrupt:
            print("\nProgram stopped by user.")
            break


if __name__ == "__main__":
    main()
