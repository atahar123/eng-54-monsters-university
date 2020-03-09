from monsters import *
from monster_workshop import *
from student import *
from teacher import *

# i want to show that i can create a student with only first and last name

# student1 = Student('John', 'Connor', 1)
# student2 = Student('Kevin', 'Jones', 2)
#
# print(student1)
# print(student1.f_name, student1.l_name)
# print(student2)
# print(student2.f_name, student2.l_name)
#
#
#
# while True:

#     student3 = Student(f_name, l_name, 3)
#     print(student3.f_name + student3.l_name)

# for student in list_students_created:
#     print(student1.f_name, student1.l_name, student2.f_name, student2.l_name)
print('==========Adding a student==========')
students_list = []
student_id = 0
while True:
    student_id += 1
    f_name = input('Enter first name\n')
    l_name = input('Enter last name\n')
    skills = input('Enter skills\n')
    student = Student(f_name, l_name, student_id, skills)
    students_list.append(student)

    print(f'Student Name is {f_name} {l_name} {student_id}')
    print(students_list)
    print('Number of students in the list: ' + str(len(students_list)))
    print(f'Skills are {skills}')

    if f_name == 'Quit' or l_name == 'Quit':
        break

#
#
#
#
#
#
# teacher1 = Teacher('Mr', 'Johnson', 1)
# teacher2 = Teacher('Mrs', 'Daniels', 2)
#
# print(teacher1)
# print(teacher1.f_name, teacher1.l_name)
# print(teacher2)
# print(teacher2.f_name, teacher2.l_name)
#
# list_teachers_created = []
# list_teachers_created.append(teacher1)
# list_teachers_created.append(teacher2)
#
# for teacher in list_teachers_created:
#     print(teacher1.f_name, teacher1.l_name, teacher2.f_name, teacher2.l_name)
#
#
#
#
#
#
print('==========Adding a teacher==========')
teachers_list = []
teacher_id = 0
while True:
    teacher_id += 1
    f_name = input('Enter first name\n')
    l_name = input('Enter last name\n')
    teacher = Teacher(f_name, l_name, teacher_id, skills)
    teachers_list.append(teacher)

    print(f'Teacher Name is {f_name} {l_name} {teacher_id}')
    print(teachers_list)
    print('Number of teachers in the list: ' + str(len(teachers_list)))

    if f_name == 'Quit' or l_name == 'Quit':
        break
#
#
#
#
#
#
print('==========Adding a workshop==========')
workshop_list = []
while True:
    subject_name = input('Enter subject name:\n')
    teacher_name = input('Enter teacher name\n')
    attendees = input('Enter number of attendees\n')
    subject = Monster_Workshop(subject_name, teacher_name, attendees)
    workshop_list.append(subject)

    print(f'Workshop added was: {subject} and teacher\'s name is {teacher_name}. Attendees are {attendees}')
    print(workshop_list)
    print('Number of workshops in the list: ' + str(len(workshop_list)))

    if subject_name == 'Quit' or teacher_name == 'Quit' or attendees == 'Quit':
        break
#
#
#
#
#
#
print(workshop_list)
#
#
#
#
#
#
