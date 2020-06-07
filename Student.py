class Student(object):
    def __init__(self, first='', last='', student_id=0):
        self.first_name_str = first
        self.last_name_str = last
        self.student_id_int = student_id

    def update(self, first='', last='', student_id=0):
        if first:
            self.first_name_str = first
        if last:
            self.last_name_str = last
        if student_id:
            self.student_id_int = student_id

    def __str__(self):
        return "{}  {}, ID: {}". \
            format(self.first_name_str, self.last_name_str, self.student_id_int)
