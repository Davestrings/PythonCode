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


def main ():
    student1 = Student("James", "Bond", 189)
    student2 = Student("Anthony", "Joshua")
    print(student1)
    print(student2)
    print('Updated Record')
    print('='*20)
    student1.update(student_id=134)
    print(student1)
    student2.update(student_id=189)
    print(student2)


main()

