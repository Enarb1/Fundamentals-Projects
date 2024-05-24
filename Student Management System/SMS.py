# Dictionary to store student records
students = {}


def add_student(name, age, grade, subjects):
    if name in students:
        print(f"Student {name} already exists. Choose another name or update existing")
        return
    else:
        students[name] = {'age': age, 'grade': grade, 'subjects': subjects}
        print(f"Student {name} added successfully.")

# Checks if student exists
# Adding the new student to the dictionary


def update_student(name):
    if name not in students:
        print(f"Student {name} doesn't exist")
        return
    student = students[name]

    new_age = input(f"Enter age for {name} (current age{student["age"]})")
    if new_age:
        student['age'] = int(new_age)
    new_grade = input(f"Enter the new grade for {name} (current grade: {student['grade']})")
    if new_grade:
        student['grade'] = float(new_grade)
    new_subjects = input(f"Enter the new subjects separated by commas for {name} (current subjects: {", ".join(student['subjects'])})")
    if new_subjects:
        student['subjects'] = [subject.strip() for subject in new_subjects.split(',')]

    students[name] = student
    print(f"{name} has been updated")
    # Checks if the student exists
    # Prompts the user to update fields and keep current values if fields are empty
    # Updates the new values, if there are any


def delete_student(name):
    if name not in students:
        print(f"Student {name} doesn't exist")
        return
    del students[name]
    print("Entry has been deleted")

    # Checks if the student exists
    # Deletes the student's record


def search_student(name):
    if name not in students:
        print(f"Student {name} doesn't exist")
        return None
    else:
        student = students[name]
        print(f"Name: {name}")
        print(f"Age: {students['age']}")
        print(f"Grade: {students['grade']}")
        print("Subjects:", ', '.join(students['subjects']))
        return student

    # Checks if the student exists
    # Returns the student's record


def list_all_students():
    if not students:
        print("No student records available.")
    else:
        print("List of all students:")
        for name, info in students.items():
            print(f"Name: {name}")
            print(f"Age: {info['age']}")
            print(f"Grade: {info['grade']}")
            print("Subjects:", ', '.join(info['subjects']))
            print()
    # Checks if there are any student records
    # Lists all students


def main():
    """
    Main function to provide user interaction.
    """
    while True:
        # Display menu options
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. List All Students")
        print("6. Exit")

        # Prompt user for their choice
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for student details
            name = input("Enter student's name: ")
            age = int(input("Enter student's age: "))
            grade = float(input("Enter student's grade: "))
            subjects = input("Enter student's subjects (comma-separated): ").split(',')
            # Call the add_student function
            add_student(name, age, grade, subjects)
        elif choice == '2':
            # Prompt for student name to update
            name = input("Enter student's name to update: ")
            # Call the update_student function
            update_student(name)
        elif choice == '3':
            # Prompt for student name to delete
            name = input("Enter student's name to delete: ")
            # Call the delete_student function
            delete_student(name)
        elif choice == '4':
            # Prompt for student name to search
            name = input("Enter student's name to search: ")
            # Call the search_student function
            search_student(name)
        elif choice == '5':
            # Call the list_all_students function
            list_all_students()
        elif choice == '6':
            # Exit the program
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
