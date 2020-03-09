from monsters import *


class Student(Monsters):

    def __init__(self, f_name, l_name, student_id, skills):
        super().__init__(f_name, l_name, skills)
        self.student_id = student_id
        self.skills = skills
