# problem1_backtracking.py
# python3 ./src/problem1_backtracking.py
# Time complexity: O(N!) 
# Speed Complexity: O(N^2)

# Ayden Deng
# ID: 2121072
# E-mail: ydeng24@depaul.edu

def print_board(board):
    for row in board:
        print(" ".join(str(col) for col in row))
    print("\n")

def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens(board, row):
    if row >= len(board):
        return True
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve_n_queens(board, row + 1):
                return True
            board[row][col] = 0
    return False

def main():
    n = 8
    board = [[0 for _ in range(n)] for _ in range(n)]
    if solve_n_queens(board, 0):
        print_board(board)
    else:
        print("No solution found")

if __name__ == "__main__":
    main()
