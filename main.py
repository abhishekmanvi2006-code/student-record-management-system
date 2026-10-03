import json

FILE_NAME = "students.json"


def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def add_student():
    students = load_students()

    try:
        student_id = int(input("Enter student ID: "))
        age = int(input("Enter age: "))
    except ValueError:
        print("ID and age must be numbers.")
        return

    name = input("Enter name: ")
    course = input("Enter course: ")

    if any(student["id"] == student_id for student in students):
        print("Student ID already exists.")
        return

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    save_students(students)

    print("Student added successfully.")


def view_students():
    students = load_students()

    if not students:
        print("No student records found.")
        return

    for student in students:
        print(
            f"ID: {student['id']} | "
            f"Name: {student['name']} | "
            f"Age: {student['age']} | "
            f"Course: {student['course']}"
        )


def update_student():
    students = load_students()

    try:
        student_id = int(input("Enter student ID to update: "))
    except ValueError:
        print("Invalid ID.")
        return

    for student in students:
        if student["id"] == student_id:
            student["name"] = input("Enter new name: ")

            try:
                student["age"] = int(input("Enter new age: "))
            except ValueError:
                print("Invalid age.")
                return

            student["course"] = input("Enter new course: ")

            save_students(students)
            print("Student updated successfully.")
            return

    print("Student not found.")


def delete_student():
    students = load_students()

    try:
        student_id = int(input("Enter student ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return

    new_students = [
        student for student in students
        if student["id"] != student_id
    ]

    if len(new_students) == len(students):
        print("Student not found.")
        return

    save_students(new_students)
    print("Student deleted successfully.")


def main():
    while True:
        print("\n--- Student Record Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()