class Solution:
    def numTilings(self, n: int) -> int:
        """
        Calculate the number of ways to tile a 1 x n board using 2 x 1 and 1 x 2 tiles.

        The function takes an integer `n` as input and returns the number of ways to tile a 1 x n board using 2 x 1 and 1 x 2 tiles.

        The function uses a dynamic programming approach to calculate the number of ways to tile the board. It uses an array `f` to keep track of the number of ways to tile a 1 x i board, for i in [0, n].

        The function initializes the array `f` with `[1, 0, 0, 0]` and a modulus value `mod`. The loop iterates from `i = 1` to `i = n`, and for each iteration, it calculates the number of ways to tile a 1 x i board using the previous 4 elements of the `f` array. The result is then stored in the `g` array and updated in the `f` array for the next iteration.

        The function returns the first element of the `f` array after the loop.

        Args:
            n: An integer representing the size of the 1 x n board.

        Returns:
            An integer representing the number of ways to tile a 1 x n board using 2 x 1 and 1 x 2 tiles.

        Raises:
            None

        Example:
            >>> s = Solution()
            >>> s.numTilings(3)
            5
            
        Time Complexity : O(n), as we are calculating f[0], f[1] ... f[n], the loop iterates at most n times, and each ietration takes conatsnt time.
        Space Complexity : O(1),  because the f array is used as a lookup table.

        """
        f = [1, 0, 0, 0]
        mod = 10**9 + 7
        for i in range(1, n + 1):
            g = [0] * 4
            g[0] = (f[0] + f[1] + f[2] + f[3]) % mod
            g[1] = (f[2] + f[3]) % mod
            g[2] = (f[1] + f[3]) % mod
            g[3] = f[0]
            f = g
        return f[0]