def countBits(self, n:int) -> List[int]:
    """
    Count the number of set bits (i.e., 1's) in the binary representation of each integer from 0 to n.

    Args:
    - n (int): The maximum integer to consider, inclusive.

    Returns:
    - List[int]: A list of integers where the ith element is the number of set bits in the binary representation of i.
    
    Time Complexity : O(n), since constant-time operation for each element in the list 'ans'.
    Space Complexity: O(n), since we allocate a list of length 'n+1' to store the results.
    """
    ans = [0]*(n+1)
    for i in range(1, n+1):
        ans[i] = ans[i & (i-1)]+1
    return ans