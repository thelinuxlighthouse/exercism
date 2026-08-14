from itertools import combinations


def rectangles(strings):
    if not strings:
        return 0

    plus_coordinates = []

    # Find every '+' coordinate.
    for row in range(len(strings)):
        for col in range(len(strings[row])):
            if strings[row][col] == "+":
                plus_coordinates.append((row, col))

    # Find every valid horizontal side.
    horizontal_sides = []

    for first, second in combinations(plus_coordinates, 2):
        # Both '+' characters must be on the same row.
        if first[0] != second[0]:
            continue

        # Everything between them must be '-' or '+'.
        between = strings[first[0]][first[1] + 1:second[1]]

        if all(character in "-+" for character in between):
            horizontal_sides.append((first, second))

    rectangle_count = 0

    # Take two horizontal sides and see whether they form
    # the top and bottom of a rectangle.
    for first_side, second_side in combinations(horizontal_sides, 2):
        first_left, first_right = first_side
        second_left, second_right = second_side

        # The left and right columns must line up.
        if (
            first_left[1] != second_left[1]
            or first_right[1] != second_right[1]
        ):
            continue

        # They must be on different rows.
        if first_left[0] == second_left[0]:
            continue

        top_row = min(first_left[0], second_left[0])
        bottom_row = max(first_left[0], second_left[0])

        left_col = first_left[1]
        right_col = first_right[1]

        # Check the left vertical side.
        left_side = all(
            strings[row][left_col] in "|+"
            for row in range(top_row + 1, bottom_row)
        )

        # Check the right vertical side.
        right_side = all(
            strings[row][right_col] in "|+"
            for row in range(top_row + 1, bottom_row)
        )

        if left_side and right_side:
            rectangle_count += 1

    return rectangle_count