STUDENTS = [
    'Alice', 'Bob', 'Charlie', 'David',
    'Eve', 'Fred', 'Ginny', 'Harriet',
    'Ileana', 'Joseph', 'Kincaid', 'Larry'
    ]

PLANTS = {
    'C': 'Clover',
    'G': 'Grass',
    'R': 'Radishes',
    'V': 'Violets',
    }


class Garden:
    def __init__(self, diagram, students=STUDENTS):
        self.diagram = diagram
        self.students = sorted(students)

    def plants(self, student):
        row1, row2 = self.diagram.split('\n')

        plnts = []
        for p in range(0, len(row1), 2):
            plnts.append([PLANTS[p] for p in row1[p:p+2]+row2[p:p+2]])
        students_plants = dict(zip(self.students, plnts))
        return students_plants[student]
