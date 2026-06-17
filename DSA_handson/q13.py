def find_student(students, name_to_find):
    for student in students:
        if student == name_to_find:
            return "Student found in the class!"
    return "Student not found."

student_list = input("Enter student names separated by spaces: ").split()
student_target = input("Which student are you looking for? ")
print(find_student(student_list, student_target))