import json
from datetime import datetime

FILE_NAME = "students.json"


def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def get_valid_age():
    while True:
        try:
            age = int(input("Enter Age: "))
            if age <= 0:
                print("Age must be greater than 0.")
                continue
            return age
        except ValueError:
            print("Please enter a valid age.")


def get_valid_marks():
    while True:
        try:
            marks = float(input("Enter Marks: "))
            if 0 <= marks <= 100:
                return marks
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter valid marks.")


def add_student(students):
    student_id = input("Enter Student ID: ")

    if student_id in students:
        print("Student already exists.")
        return

    name = input("Enter Name: ")
    age = get_valid_age()
    marks = get_valid_marks()

    students[student_id] = {
        "name": name,
        "age": age,
        "marks": marks,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    save_students(students)
    print("Student added successfully.")


def view_students(students):
    if not students:
        print("No student records found.")
        return

    print("\n========== STUDENT RECORDS ==========")

    for sid, details in students.items():
        print("-----------------------------------")
        print(f"ID         : {sid}")
        print(f"Name       : {details['name']}")
        print(f"Age        : {details['age']}")
        print(f"Marks      : {details['marks']}")
        print(f"Created On : {details.get('created_at', 'Not Available')}")
        print("-----------------------------------")


def search_student(students):
    student_id = input("Enter Student ID: ")

    if student_id in students:
        details = students[student_id]

        print("\nStudent Found")
        print("-----------------------------------")
        print(f"Name  : {details['name']}")
        print(f"Age   : {details['age']}")
        print(f"Marks : {details['marks']}")
        print("-----------------------------------")
    else:
        print("Student not found.")


def search_by_name(students):
    name = input("Enter Student Name: ").lower()

    found = False

    for sid, details in students.items():
        if details["name"].lower() == name:
            
            print("\nStudent Found")
            print("-----------------------------------")
            print(f"ID     : {sid}")
            print(f"Name   : {details['name']}")
            print(f"Age    : {details['age']}")
            print(f"Marks  : {details['marks']}")
            print("-----------------------------------")
            found = True

    if not found:
        print("Student not found.")


def update_student(students):
    student_id = input("Enter Student ID to update: ")

    if student_id not in students:
        print("Student not found.")
        return

    students[student_id]["name"] = input("Enter New Name: ")
    students[student_id]["age"] = get_valid_age()
    students[student_id]["marks"] = get_valid_marks()

    save_students(students)
    print("Student updated successfully.")


def delete_student(students):
    student_id = input("Enter Student ID to delete: ")

    if student_id in students:
        del students[student_id]
        save_students(students)
        print("Student deleted successfully.")
    else:
        print("Student not found.")


def total_students(students):
    print(f"\nTotal Students: {len(students)}")


def marks_report(students):
    if not students:
        print("No student records found.")
        return

    marks = [student["marks"] for student in students.values()]

    print("\n========== MARKS REPORT ==========")
    print(f"Highest Marks : {max(marks)}")
    print(f"Lowest Marks  : {min(marks)}")
    print(f"Average Marks : {round(sum(marks)/len(marks), 2)}")


students = load_students()

while True:
    print("\n===================================")
    print("   STUDENT MANAGEMENT SYSTEM")
    print("===================================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student By ID")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Search Student By Name")
    print("7. Total Students")
    print("8. Marks Report")
    print("9. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_student(students)

    elif choice == "2":
        view_students(students)

    elif choice == "3":
        search_student(students)

    elif choice == "4":
        update_student(students)

    elif choice == "5":
        delete_student(students)

    elif choice == "6":
        search_by_name(students)

    elif choice == "7":
        total_students(students)

    elif choice == "8":
        marks_report(students)

    elif choice == "9":
        print("Thank you for using Student Management System.")
        break

    else:
        print("Invalid choice. Please try again.")