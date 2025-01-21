'''According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.

Given the current state of the board, update the board to reflect its next state.

Note that you do not need to return anything.

 

Example 1:


Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
Example 2:


Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
 '''

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        # Helper function to count live neighbors
        def count_live_neighbors(r, c):
            directions = [
                (-1, -1), (-1, 0), (-1, 1),  # Top row neighbors
                (0, -1),         (0, 1),     # Left and right neighbors
                (1, -1), (1, 0), (1, 1)      # Bottom row neighbors
            ]
            live_neighbors = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and abs(board[nr][nc]) == 1:
                    live_neighbors += 1
            return live_neighbors

        # First pass: Apply the rules and encode the transitions
        for r in range(rows):
            for c in range(cols):
                live_neighbors = count_live_neighbors(r, c)

                # Apply rules for live cells
                if board[r][c] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[r][c] = -1  # Live cell dies

                # Apply rules for dead cells
                elif board[r][c] == 0:
                    if live_neighbors == 3:
                        board[r][c] = 2  # Dead cell becomes alive

        # Second pass: Decode the board to the final state
        for r in range(rows):
            for c in range(cols):
                if board[r][c] > 0:  # Alive in the next state
                    board[r][c] = 1
                else:  # Dead in the next state
                    board[r][c] = 0