
students = [("Allen Anderson", "Computer Science"),
            ("Edgar Einstein", "Engineering"),
            ("Farrah Finn", "Fine Arts")]

def add_new_student(students, name, major):
    students.append((name, major))

def update_student(students, index, name, major):
    students[index] = name, major

def find_students_by_name(students, name):
    return [student for student in students if name in student[0]]

def get_all_majors(students):
    return [student[1] for student in students]

# In the update_student function, the '(' and ')' parentheses can be removed without causing any errors.

print(students)
update_student(students, 1, 'John', 'Computer Programming')
print(students)

print(find_students_by_name(students, 'Resul'))

add_new_student(students, 'Joey', 'Computer Science')
print(students)


"""
[True] In the update_student function, the '(' and ')' parentheses can be removed without causing any errors.
[True] Calling find_students_by_name(students, 'in') returns a list of 2 tuples.
[True] The add_new_student function adds a new student in the last place in the list.
"""
