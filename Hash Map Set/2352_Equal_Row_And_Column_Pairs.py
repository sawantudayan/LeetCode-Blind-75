def equalPairs(self, grid: List[List[int]]) -> int:
    """
    This function returns the number of equal pairs of rows and columns in the given grid.
    Two pairs (grid[i], grid[j]) and (grid[k], grid[l]) are considered equal if the corresponding elements in the rows and columns are equal, i.e., grid[i][a] == grid[k][a] and grid[b][i] == grid[b][k] for all valid a and b.
   
    Parameters:
    grid (List[List[int]]): A list of list of integers representing the grid. The grid is a square matrix with dimensions n x n.

    Returns:
    int: The number of equal pairs of rows and columns in the grid.

    Time Complexity: O(n^3), the function has three nested loops, with two of them iterating up to n (for rows and columns), and the third one iterating up to n^2 (for all valid elements in the rows and columns). Therefore, the time complexity is O(n^3).

    Space Complexity: O(1), the function does not use any additional space that scales with the size of the input
    """
    n = len(grid)
    ans = 0
    for i in range(n):
        for j in range(n):
            ans = ans + all(grid[i][k] == grid[k][j] for k in range(n))
    return ans