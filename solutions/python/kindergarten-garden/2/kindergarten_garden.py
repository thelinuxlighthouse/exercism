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
        self.students_plants = self.students_and_plants()

    def plants(self, student):
        return self.students_plants[student]

    def students_and_plants(self):
        row1, row2 = self.diagram.split('\n')
        plants = []
        for p in range(0, len(row1), 2):
            plants.append([PLANTS[p] for p in row1[p:p+2]+row2[p:p+2]])
        return dict(zip(self.students, plants))
