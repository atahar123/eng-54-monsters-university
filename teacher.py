from monsters import *


class Teacher(Monsters):

    def __init__(self, f_name, l_name, teacher_id, skills):
        super().__init__(f_name, l_name, skills)
        self.teacher_id = teacher_id
        self.skills = skills
