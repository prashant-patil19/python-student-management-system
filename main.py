import json

FILE_NAME = "students.json"


def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return {}


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def add_student(students):
    student_id = input("Enter ID: ")

    if student_id in students:
        print("Student already exists.")
        return

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    marks = float(input("Enter Marks: "))

    students[student_id] = {
        "name": name,
        "age": age,
        "marks": marks
    }

    save_students(students)
    print("Student added successfully.")


def view_students(students):
    if not students:
        print("No records found.")
        return

    for sid, details in students.items():
        print("\nID:", sid)
        print("Name:", details["name"])
        print("Age:", details["age"])
        print("Marks:", details["marks"])


def search_student(students):
    student_id = input("Enter ID to search: ")

    if student_id in students:
        details = students[student_id]
        print("Name:", details["name"])
        print("Age:", details["age"])
        print("Marks:", details["marks"])
    else:
        print("Student not found.")


def update_student(students):
    student_id = input("Enter ID to update: ")

    if student_id not in students:
        print("Student not found.")
        return

    students[student_id]["name"] = input("New Name: ")
    students[student_id]["age"] = int(input("New Age: "))
    students[student_id]["marks"] = float(input("New Marks: "))

    save_students(students)
    print("Student updated successfully.")


def delete_student(students):
    student_id = input("Enter ID to delete: ")

    if student_id in students:
        del students[student_id]
        save_students(students)
        print("Student deleted successfully.")
    else:
        print("Student not found.")


students = load_students()

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

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
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")