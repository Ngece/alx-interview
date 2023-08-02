#!/usr/bin/python3
"""N Queens program"""

import sys

def is_safe(board, row, col, N):
    """ Check if there is a queen in the 
    same column or on the same diagonal
    """
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

# Function to recursively solve the N Queens problem using backtracking
def solve_n_queens(board, row, N):
    """ Base case: If all rows have been explored, print the solution"""
    if row == N:
        print([[i, board[i]] for i in range(N)])
        return

    for col in range(N):
        """ Try placing the queen in each column of the current row"""
        if is_safe(board, row, col, N):
            board[row] = col
            solve_n_queens(board, row + 1, N)
            board[row] = -1


def n_queens(N):
    """ Function to initialize the chessboard and start the backtracking process"""
    board = [-1 for _ in range(N)]
    solve_n_queens(board, 0, N) 

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)

        n_queens(N)

    except ValueError:
        print("N must be a number")
        sys.exit(1)