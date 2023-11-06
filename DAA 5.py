def is_safe(board, row, col, n):
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col, n):
    if col >= n:
        return True

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1

            if solve_n_queens(board, col + 1, n):
                return True

            board[i][col] = 0

    return False

def print_solution(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()

n = int(input("Enter the value of n (the size of the n-queens board): "))
first_queen_row = int(input("Enter the row where the first queen is placed (0-based index): "))

if first_queen_row < 0 or first_queen_row >= n:
    print("Invalid input for the first queen's row. It should be within the range [0, n-1].")
else:
    # Initialize the n-queens board
    board = [[0] * n for _ in range(n)]
    board[first_queen_row][0] = 1

    if solve_n_queens(board, 1, n):
        print("Solution exists. The final n-queens matrix:")
        print_solution(board, n)
    else:
        print("No solution exists for the given configuration.")
