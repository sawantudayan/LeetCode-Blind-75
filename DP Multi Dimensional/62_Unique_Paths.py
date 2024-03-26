class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        This method calculates the number of unique paths from the top-left corner to the bottom-right corner of a grid with dimensions m x n.
        The grid has obstacles represented by 1's and empty spaces represented by 0's. This method assumes that the top-left and bottom-right corners are always empty spaces.
        The method uses dynamic programming to calculate the number of unique paths by filling up a 2D array `f` where f[i][j] is the number of unique paths to reach the cell at row i and column j. The value of each cell is calculated as the sum of the number of unique paths to the left cell and the number of unique paths to the top cell. The final answer is the value of the bottom-right cell in the array `f`. If the input grid contains obstacles, the method will return 0 as there will be no unique paths to the bottom-right corner of the grid. The time complexity of this method is O(m*n) and the space complexity is O(m*n).
        Parameters:
        - m: The number of rows in the grid.
        - n: The number of columns in the grid.
        Returns:
        The number of unique paths from the top-left corner to the bottom-right corner of the grid. If the grid contains obstacles, the method returns 0.
        
        
        Time Complexity : O(m*n), where m and n are the number of rows and coluns in the input grid
        Space  Complexity: O(m*n), due to array 'f' that stores the number of unique paths to rach each cell.
        
        """
        f = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i - 1][j] + f[i][j - 1]
        return f[-1][-1]