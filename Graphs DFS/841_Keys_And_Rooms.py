def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
    """
    This function checks if it is possible to visit all rooms in a given list of rooms.
    A room can be visited if we have already visited its key.
    We use Depth First Search (DFS) to explore all rooms recursively.

    :param self: instance of the class
    :param rooms: List[List[int]] - A list of lists representing the rooms. Each room is a list of keys that can be used to enter other rooms.
    :return: bool - True if it is possible to visit all rooms, False otherwise.
    
    Time Complexity : O(m+n), where n is the number of nodes, and m is the number of edges
    Space Complexity : O(n)
    
    
    """
    def dfs(i: int) -> None:
        """
        Depth First Search (DFS) helper function to visit all reachable rooms from the current room.

        :param i: int - Index of the current room
        :return: None
        """
        if i in vis:
            return
        vis.add(i)
        for j in rooms[i]:
            dfs(j)

    vis = set()  # Initialize a set to keep track of visited rooms
    dfs(0)  # Start the DFS from the first room (index 0)
    return len(vis) == len(rooms)  # Return True if all rooms are visited, False otherwise.