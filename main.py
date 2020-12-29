# Back tracking algorithm:
# 1: pick an empty square
# 2: try numbers in that square
# 3: until you find a number that fits
# 4: move to next empty square
# 5: when you find an empty square with no numbers that fit
# backtrack to the last filled box and try more numbers in that square until you find another that fits
# 6: if no numbers fit in this square backtrack again.
# 7: repeat until you can change a square
# 8: if you reach the end of the grid , the sudoku is solved

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print(" - - - - - - - - - - - ")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty_square(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j  # row, col

    return None


def board_is_valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check 3x3
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def solve(bo):
    find = find_empty_square(bo)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if board_is_valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


print_board(board)
print("\nsolving...")
solve(board)
print("\n-----------------------------\n")
print("solved!\n")
print_board(board)
