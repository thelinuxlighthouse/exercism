class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = [[int(l) for l in li.split()] for li in matrix_string.split('\n')]

    def row(self, index):
        return self.matrix_string[index-1]

    def column(self, index):
        return [l[index-1] for l in self.matrix_string]
