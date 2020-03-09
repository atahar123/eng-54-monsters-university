from monsters import *
from monster_workshop import *
from student import *
from teacher import *

# i want to show that i can create a student with only first and last name

student1 = Student('John', 'Connor', 1)
student2 = Student('Kevin', 'Jones', 2)

print(student1)
print(student1.f_name, student1.l_name)
print(student2)
print(student2.f_name, student2.l_name)

list_students_created = []
list_students_created.append(student1)
list_students_created.append(student2)

for student in list_students_created:
    print(student1.f_name, student1.l_name, student2.f_name, student2.l_name)
#
#
#
#
#
#
teacher1 = Teacher('Mr', 'Johnson', 1)
teacher2 = Teacher('Mrs', 'Daniels', 2)

print(teacher1)
print(teacher1.f_name, teacher1.l_name)
print(teacher2)
print(teacher2.f_name, teacher2.l_name)

list_teachers_created = []
list_teachers_created.append(teacher1)
list_teachers_created.append(teacher2)

for teacher in list_teachers_created:
    print(teacher1.f_name, teacher1.l_name, teacher2.f_name, teacher2.l_name)
#
#
#
#
#
#

