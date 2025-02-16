'''The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example 1:
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

Example 2:
Input: n = 1
Output: 1'''

def totalNQueens(n):
    count = 0
    col = set()  # Tracks used columns
    posDiag = set()  # Tracks used positive diagonals (row + col)
    negDiag = set()  # Tracks used negative diagonals (row - col)

    def backtrack(r):
        nonlocal count
        if r == n:  # If all queens are placed, count as a solution
            count += 1
            return
        
        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue  # Skip invalid positions
            
            # Place queen
            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)

            backtrack(r + 1)  # Recur to next row

            # Remove queen (backtrack)
            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)

    backtrack(0)
    return count