from collections import defaultdict 


class School:
    def __init__(self):
        self.students = defaultdict(list)

    def add_student(self, name, grade):
        self.students[grade].append(name)

    def roster(self):
        s = []
        for k in sorted(self.students):
            s.extend(self.grade(k))
        return s

    def grade(self, grade_number):
        return sorted(self.students[grade_number])
