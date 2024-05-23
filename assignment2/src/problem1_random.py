# problem1_random.py
# python3 ./src/problem1_random.py
# Time complexity: This complexity is typically polynomial - In the worst case, it might need to run infinite adjustments, but in general, it is usually faster than O(N!). The specific complexity is hard to define strictly but is typically polynomial in nature.
# Speed Complexity: O(N)

# Ayden Deng
# ID: 2121072
# E-mail: ydeng24@depaul.edu

import random

def print_board(board):
    for row in board:
        print(" ".join(str(col) for col in row))
    print("\n")

def calculate_conflicts(board):
    conflicts = [0] * len(board)
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                conflicts[i] += 1
                conflicts[j] += 1
    return conflicts

def solve_n_queens_random(n):
    board = [random.randint(0, n - 1) for _ in range(n)]
    while True:
        conflicts = calculate_conflicts(board)
        if max(conflicts) == 0:
            return board
        max_conflict = max(conflicts)
        max_conflict_queens = [i for i, x in enumerate(conflicts) if x == max_conflict]
        queen = random.choice(max_conflict_queens)
        new_position = random.randint(0, n - 1)
        while new_position == board[queen]:
            new_position = random.randint(0, n - 1)
        board[queen] = new_position

def main():
    n = 8
    board = solve_n_queens_random(n)
    solution = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        solution[i][board[i]] = 1
    print_board(solution)

if __name__ == "__main__":
    main()
