
def saddle_points(matrix):
    if len(set([len(row) for row in matrix])) > 1:
        raise ValueError("Matrix can't be irregular")
    result = []
    for row, row_data in enumerate(matrix, 1):
        for column, col_data in enumerate(row_data, 1):
            if max(row_data) == min([row[column-1] for row in matrix]):
                result.append({'row': row, 'column': column})
    return result

