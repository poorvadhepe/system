def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

def print_board(board):
    for row in board:
        print(''.join(row))
    print()

# Standard Backtracking
def solve_n_queens_backtracking(res, board, row, n):
    if row == n:
        res.append([''.join(r) for r in board])
        print_board(board)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'
            print_board(board)
            solve_n_queens_backtracking(res, board, row + 1, n)
            board[row][col] = '.'  # Backtrack

# Optimized Branch and Bound
def solve_n_queens_branch_bound(res, board, row, n, left_row, upper_diag, lower_diag):
    if row == n:
        res.append([''.join(r) for r in board])
        return

    for col in range(n):
        if not left_row[col] and not upper_diag[row + col] and not lower_diag[n - 1 + col - row]:
            board[row][col] = 'Q'
            left_row[col] = upper_diag[row + col] = lower_diag[n - 1 + col - row] = 1

            solve_n_queens_branch_bound(res, board, row + 1, n, left_row, upper_diag, lower_diag)

            board[row][col] = '.'
            left_row[col] = upper_diag[row + col] = lower_diag[n - 1 + col - row] = 0

# Main function
def main():
    n = int(input("Enter the value of n: "))

    board = [['.' for _ in range(n)] for _ in range(n)]
    res = []

    print("\n--- Solving with Backtracking ---")
    solve_n_queens_backtracking(res, board, 0, n)

    print("All possible solutions (Backtracking):")
    for solution in res:
        for row in solution:
            print(row)
        print()

    # Clear results and prepare for optimized
    res.clear()
    board = [['.' for _ in range(n)] for _ in range(n)]
    left_row = [0] * n
    upper_diag = [0] * (2 * n - 1)
    lower_diag = [0] * (2 * n - 1)

    print("\n--- Solving with Branch and Bound ---")
    solve_n_queens_branch_bound(res, board, 0, n, left_row, upper_diag, lower_diag)

    print("All possible solutions (Branch and Bound):")
    for solution in res:
        for row in solution:
            print(row)
        print()

if __name__ == "__main__":
    main()
