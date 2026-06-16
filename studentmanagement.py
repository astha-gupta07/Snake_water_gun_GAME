# Student Management System

students = []

# Add Student
def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    student = {
        "Roll": roll,
        "Name": name,
        "Age": age,
        "Course": course
    }

    students.append(student)
    print("Student Added Successfully!")

# View Students
def view_students():
    if len(students) == 0:
        print("No Student Records Found!")
    else:
        print("\nStudent Records:")
        for student in students:
            print("-------------------------")
            print("Roll No :", student["Roll"])
            print("Name    :", student["Name"])
            print("Age     :", student["Age"])
            print("Course  :", student["Course"])

# Search Student
def search_student():
    roll = input("Enter Roll Number to Search: ")

    for student in students:
        if student["Roll"] == roll:
            print("\nStudent Found")
            print(student)
            return

    print("Student Not Found!")

# Update Student
def update_student():
    roll = input("Enter Roll Number to Update: ")

    for student in students:
        if student["Roll"] == roll:
            student["Name"] = input("Enter New Name: ")
            student["Age"] = input("Enter New Age: ")
            student["Course"] = input("Enter New Course: ")

            print("Student Updated Successfully!")
            return

    print("Student Not Found!")

# Delete Student
def delete_student():
    roll = input("Enter Roll Number to Delete: ")

    for student in students:
        if student["Roll"] == roll:
            students.remove(student)
            print("Student Deleted Successfully!")
            return

    print("Student Not Found!")

# Main Menu
while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Try Again.")