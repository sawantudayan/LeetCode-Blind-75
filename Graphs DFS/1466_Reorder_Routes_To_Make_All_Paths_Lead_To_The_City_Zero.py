def minReorder(self, n: int, connections: List[List[int]]) -> int:
    """
    This function performs a depth-first-search (dfs) on a graph to find the minimum number of rewiring needed to make the graph connected.

    Parameters:
    n (int): The number of nodes in the graph.
    connections (List[List[int]]): A list of connections between nodes, represented as a list of lists, where each inner list contains two nodes representing the connection.

    Returns:
    int: The minimum number of rewirings needed.
    
    Time Complexity : O(m), where m is the number of the edges.
    Space Complexity: O(n), since the active call frames on the stack is 'n'.
    """
    def dfs(a: int, fa: int) -> int:
        """
        A helper function for the minReorder function that performs the depth-first-search on the graph.

        Parameters:
        a (int): The current node in the graph.
        fa (int): The parent node of the current node.

        Returns:
        int: The sum of the weights of the edges that are connected to the current node and its descendants.
        """
        sum_val = 0
        for b, c in g[a]:
            if b != fa:
                sum_val += c + dfs(b, a)
        return sum_val

    g = [[] for _ in range(n)]
    for a, b in connections:
        g[a].append((b, 1))
        g[b].append((a, 0))
    return dfs(0, -1)