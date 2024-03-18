class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        """
        Given a 2D grid of characters maze and an initial position entrance,
        return the shortest distance to an exit from the entrance. An exit
        is any location in maze where the character is either 'E' or an
        empty space '.' and is not already occupied by another character.
        The entrance is guaranteed to be not an exit. The distance is the
        number of steps to get to an exit, moving only in four directions:
        up, down, left, and right. If no exit exists, return -1.

        Parameters:
        - maze (List[List[str]]): A 2D list of characters representing the
          grid.
        - entrance (List[int]): A list of two integers [row, col] representing
          the initial position.

        Returns:
        - int: The shortest distance to an exit, or -1 if no exit exists.
        
        Time Complexity : O(MN), where M and N are the number of rows and columns in the grid
        Space Complexity : O(MN).
        
        """
        m, n = len(maze), len(maze[0])
        i, j = entrance
        q = deque([(i, j)])
        maze[i][j] = '+'
        ans = 0
        while q:
            ans += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                for a, b in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                    x, y = i + a, j + b
                    if 0 <= x < m and 0 <= y < n and maze[x][y] == '.':
                        if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                            return ans
                        q.append((x, y))
                        maze[x][y] = '+'
        return -1