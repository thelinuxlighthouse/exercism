def square(number):
    if number <= 0 or number > 64:
        raise ValueError("Number Must be positive integer.")
    chessboard_grain = dict()
    chessboard_grain[1] = 1
    chessboard_grain[2] = 2
    for i in range(3, 65, 1):
        chessboard_grain[i] = chessboard_grain[i-1] * 2
    return chessboard_grain[number]



def total():
    return sum(square(number) for number in range(1, 65, 1))
