def findCircleNum(self, isConnected: List[List[int]]) -> int:
    """
    This function implements Depth First Search (DFS) algorithm to find the number of provinces (connected components) in a map.
    Each province is represented by a node in a 2D array, 'isConnected', where isConnected[i][j] = 1 means there is a direct road between provinces i and j, 
    and isConnected[i][j] = 0 means there is no road between provinces i and j. Two provinces are connected if there is a path between them. 
    The function returns the number of connected components (provinces) in the map.

    Parameters:
    isConnected (List[List[int]]): A list of lists representing a 2D array where isConnected[i][j] = 1 if there is a road between provinces i and j, and 
                                    isConnected[i][j] = 0 otherwise.

    Returns:
    int: The number of connected components (provinces) in the map.
    
    Time Complexity : O(n^2)
    Space Complexity : O(n)
    """
    def dfs(i : int) -> None:
        """
        A helper function for DFS traversal of the graph.
        Marks the current node and its adjacent nodes as visited.

        Parameters:
        i (int): The current node to be visited.
        """
        vis[i] = True
        for j, x in enumerate(isConnected[i]):
            if not vis[j] and x:
                dfs(j)

    n = len(isConnected)
    vis = [False] * n
    ans = 0
    for