from monsters import *


class Teacher(Monsters):

    def __init__(self, f_name, l_name, teacher_id):
        super().__init__(f_name, l_name)
        self.teacher_id = teacher_id


